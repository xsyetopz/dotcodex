"""Analyze Codex rollout JSONL without exposing message or tool content by default."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable


@dataclass
class Usage:
    responses: int = 0
    input_tokens: int = 0
    cached_input_tokens: int = 0
    output_tokens: int = 0
    reasoning_output_tokens: int = 0

    def add(self, payload: dict[str, Any]) -> None:
        self.responses += 1
        for name in (
            "input_tokens",
            "cached_input_tokens",
            "output_tokens",
            "reasoning_output_tokens",
        ):
            value = payload.get(name, 0)
            if isinstance(value, int):
                setattr(self, name, getattr(self, name) + value)


@dataclass
class SessionReport:
    session: str
    session_id: str | None = None
    kind: str = "root"
    started_at: str | None = None
    ended_at: str | None = None
    tool_calls: Counter[str] = field(default_factory=Counter)
    repeated_waits: int = 0
    spawn_calls: int = 0
    excess_spawn_calls: int = 0
    invalid_forks: int = 0
    tool_failures: int = 0
    legacy_tool_failures: int = 0
    command_executions: int = 0
    command_failures: int = 0
    command_output_bytes: int = 0
    wait_cells: Counter[str] = field(default_factory=Counter)
    wait_yield_ms: Counter[int] = field(default_factory=Counter)
    excess_cell_waits: int = 0
    compactions: int = 0
    automatic_goal_continuations: int = 0
    rapid_automatic_goal_continuations: int = 0
    automatic_turns_without_change_events: int = 0
    input_errors: int = 0
    details: list[str] = field(default_factory=list)

    def serializable(self) -> dict[str, Any]:
        result = asdict(self)
        result["tool_calls"] = dict(sorted(self.tool_calls.items()))
        result["wait_cells"] = dict(sorted(self.wait_cells.items()))
        result["wait_yield_ms"] = {
            str(value): count for value, count in sorted(self.wait_yield_ms.items())
        }
        return result


def parse_arguments(payload: dict[str, Any]) -> dict[str, Any] | None:
    raw = payload.get("arguments", payload.get("input"))
    if isinstance(raw, dict):
        return raw
    if not isinstance(raw, str):
        return None
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def tool_name(payload: dict[str, Any]) -> str | None:
    if payload.get("type") not in {"function_call", "custom_tool_call"}:
        return None
    name = payload.get("name")
    return name if isinstance(name, str) else None


def output_failed(payload: dict[str, Any]) -> bool:
    if payload.get("type") not in {"function_call_output", "custom_tool_call_output"}:
        return False
    raw = payload.get("output")
    if isinstance(raw, dict):
        decoded = raw
    elif isinstance(raw, str):
        try:
            decoded = json.loads(raw)
        except json.JSONDecodeError:
            return False
    else:
        return False
    return isinstance(decoded, dict) and (
        decoded.get("isError") is True
        or (isinstance(decoded.get("exit_code"), int) and decoded["exit_code"] != 0)
    )


def compact_event(event: dict[str, Any], payload: dict[str, Any]) -> bool:
    return any(
        isinstance(name, str) and "compact" in name.lower()
        for name in (event.get("type"), payload.get("type"))
    )


def iso_timestamp(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        timestamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return timestamp if timestamp.tzinfo is not None else timestamp.replace(tzinfo=UTC)


def timestamp_text(value: object) -> str | None:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return datetime.fromtimestamp(value, UTC).isoformat().replace("+00:00", "Z")
    timestamp = iso_timestamp(value)
    return timestamp.isoformat().replace("+00:00", "Z") if timestamp else None


def event_item(payload: dict[str, Any]) -> dict[str, Any] | None:
    item = payload.get("item") if payload.get("type") == "item_completed" else None
    return item if isinstance(item, dict) else None


def command_output_size(item: dict[str, Any]) -> int:
    output = item.get("aggregated_output")
    if not isinstance(output, str):
        output = "".join(
            value
            for value in (item.get("stdout"), item.get("stderr"))
            if isinstance(value, str)
        )
    return len(output.encode()) if isinstance(output, str) else 0


def number(value: object) -> int | float | None:
    return (
        value
        if isinstance(value, (int, float)) and not isinstance(value, bool)
        else None
    )


def iter_events(path: Path, report: SessionReport) -> Iterable[dict[str, Any]]:
    try:
        handle = path.open(encoding="utf-8", errors="replace")
    except OSError:
        report.input_errors += 1
        return
    with handle:
        for line in handle:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                report.input_errors += 1
                continue
            if isinstance(event, dict):
                yield event
            else:
                report.input_errors += 1


def analyze_session(
    path: Path, aggregate: dict[tuple[str, str], Usage], include_content: bool = False
) -> SessionReport:
    report = SessionReport(path.stem)
    models: dict[object, tuple[str, str]] = {}
    seen_usage: set[tuple[object, tuple[tuple[str, object], ...]]] = set()
    previous_wait = False
    current_model = ("?", "?")
    last_task_completed_at: int | float | None = None
    latest_task_completed_at: int | float | None = None
    saw_user_message_since_completion = False
    active_automatic_turn: object | None = None
    automatic_turns_with_changes: set[object] = set()
    canonical_compactions = 0
    legacy_compactions = 0

    for event in iter_events(path, report):
        payload = event.get("payload")
        payload = payload if isinstance(payload, dict) else {}
        event_type = event.get("type")
        if event_type == "session_meta":
            session_id = payload.get("session_id", payload.get("id"))
            report.session_id = session_id if isinstance(session_id, str) else None
            report.kind = (
                "worker" if isinstance(payload.get("parent_thread_id"), str) else "root"
            )
            report.started_at = timestamp_text(payload.get("timestamp"))
        if event_type == "turn_context":
            turn_id = payload.get("turn_id")
            current_model = (
                str(payload.get("model", "?")),
                str(payload.get("effort", "?")),
            )
            models[turn_id] = current_model
        if event_type == "event_msg" and payload.get("type") == "token_count":
            info = payload.get("info")
            usage = info.get("last_token_usage") if isinstance(info, dict) else None
            if isinstance(usage, dict) and usage:
                key = (payload.get("turn_id"), tuple(sorted(usage.items())))
                if key not in seen_usage:
                    seen_usage.add(key)
                    aggregate.setdefault(
                        models.get(key[0], current_model), Usage()
                    ).add(usage)
        if event_type == "event_msg" and payload.get("type") == "task_complete":
            completed_at = number(payload.get("completed_at"))
            if completed_at is not None and (
                latest_task_completed_at is None
                or completed_at > latest_task_completed_at
            ):
                latest_task_completed_at = completed_at
                report.ended_at = timestamp_text(completed_at)
            last_task_completed_at = completed_at
            saw_user_message_since_completion = False
        if event_type == "event_msg" and payload.get("type") == "task_started":
            started_at = number(payload.get("started_at"))
            continuation_delay = (
                started_at - last_task_completed_at
                if started_at is not None and last_task_completed_at is not None
                else None
            )
            is_automatic = (
                continuation_delay is not None
                and continuation_delay >= 0
                and not saw_user_message_since_completion
            )
            last_task_completed_at = None
            if (
                active_automatic_turn is not None
                and active_automatic_turn not in automatic_turns_with_changes
            ):
                report.automatic_turns_without_change_events += 1
            if not is_automatic:
                active_automatic_turn = None
                continue
            report.automatic_goal_continuations += 1
            if continuation_delay is not None and continuation_delay <= 60:
                report.rapid_automatic_goal_continuations += 1
            active_automatic_turn = payload.get("turn_id")
        name = tool_name(payload)
        if name is not None:
            short_name = name.rsplit(".", 1)[-1]
            report.tool_calls[short_name] += 1
            is_wait = short_name == "wait_agent"
            if is_wait and previous_wait:
                report.repeated_waits += 1
            previous_wait = is_wait
            arguments = parse_arguments(payload)
            if short_name == "spawn_agent":
                report.spawn_calls += 1
                report.excess_spawn_calls = max(0, report.spawn_calls - 2)
                if (arguments or {}).get("fork_turns") != "none":
                    report.invalid_forks += 1
            if short_name == "wait" and arguments is not None:
                cell_id = arguments.get("cell_id")
                if isinstance(cell_id, str):
                    report.wait_cells[cell_id] += 1
                    report.excess_cell_waits += report.wait_cells[cell_id] > 1
                yield_time_ms = arguments.get("yield_time_ms")
                if isinstance(yield_time_ms, int) and not isinstance(
                    yield_time_ms, bool
                ):
                    report.wait_yield_ms[yield_time_ms] += 1
            if include_content:
                rendered = (
                    json.dumps(arguments, sort_keys=True) if arguments else "<unparsed>"
                )
                report.details.append(f"tool {short_name}: {rendered[:1000]}")
        if output_failed(payload):
            report.tool_failures += 1
            report.legacy_tool_failures += 1
            if include_content:
                report.details.append(
                    f"tool failure: {str(payload.get('output'))[:1000]}"
                )
        item = event_item(payload)
        if item is not None:
            item_type = item.get("type")
            if item_type in {"CommandExecution", "command_execution"}:
                report.command_executions += 1
                report.command_output_bytes += command_output_size(item)
                if item.get("status") == "failed" or (
                    isinstance(item.get("exit_code"), int) and item["exit_code"] != 0
                ):
                    report.command_failures += 1
                    report.tool_failures += 1
            if (
                active_automatic_turn is not None
                and payload.get("turn_id") == active_automatic_turn
                and item_type in {"FileChange", "file_change", "patch_apply"}
            ):
                automatic_turns_with_changes.add(active_automatic_turn)
            if item_type in {"UserMessage", "user_message"}:
                saw_user_message_since_completion = True
        if item is not None and item.get("type") in {
            "ContextCompaction",
            "context_compaction",
        }:
            canonical_compactions += 1
        elif compact_event(event, payload):
            legacy_compactions += 1
    if (
        active_automatic_turn is not None
        and active_automatic_turn not in automatic_turns_with_changes
    ):
        report.automatic_turns_without_change_events += 1
    report.compactions = canonical_compactions or legacy_compactions
    return report


def session_timestamp(path: Path) -> datetime | None:
    report = SessionReport(path.stem)
    for event in iter_events(path, report):
        if event.get("type") == "session_meta":
            payload = event.get("payload")
            return (
                iso_timestamp(payload.get("timestamp"))
                if isinstance(payload, dict)
                else None
            )
    return None


def rollout_files(
    root: Path,
    limit: int | None,
    since: datetime | None = None,
    until: datetime | None = None,
) -> list[Path]:
    try:
        files = list(root.rglob("rollout-*.jsonl")) if root.is_dir() else [root]
        selected = []
        for path in files:
            timestamp = session_timestamp(path)
            if timestamp is None:
                if since is None and until is None:
                    selected.append(path)
                continue
            if (since is None or timestamp >= since) and (
                until is None or timestamp <= until
            ):
                selected.append(path)
        selected.sort(key=lambda path: path.stat().st_mtime, reverse=True)
        return selected[:limit] if limit is not None else selected
    except OSError:
        return []


def parse_boundary(value: str) -> datetime:
    timestamp = iso_timestamp(value)
    if timestamp is None:
        raise argparse.ArgumentTypeError("expected an ISO-8601 timestamp with timezone")
    return timestamp


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "sessions", nargs="?", type=Path, default=Path.home() / ".codex/sessions"
    )
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--since", type=parse_boundary)
    parser.add_argument("--until", type=parse_boundary)
    parser.add_argument("--include-content", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")
    if args.since and args.until and args.since > args.until:
        parser.error("--since must not be after --until")
    return args


def boundary_text(value: datetime | None) -> str | None:
    return value.isoformat().replace("+00:00", "Z") if value else None


def main() -> int:
    args = parse_args()
    aggregate: dict[tuple[str, str], Usage] = {}
    reports = [
        analyze_session(path, aggregate, args.include_content)
        for path in rollout_files(args.sessions, args.limit, args.since, args.until)
    ]
    output = {
        "content_redacted": not args.include_content,
        "time_boundary": {
            "since": boundary_text(args.since),
            "until": boundary_text(args.until),
        },
        "files": len(reports),
        "usage": [
            {"model": model, "effort": effort, **asdict(usage)}
            for (model, effort), usage in sorted(
                aggregate.items(), key=lambda item: item[1].input_tokens, reverse=True
            )
        ],
        "sessions": [report.serializable() for report in reports],
    }
    if args.as_json:
        print(json.dumps(output, indent=2, sort_keys=True))
        return 0
    redaction = "redacted" if output["content_redacted"] else "included"
    boundary = output["time_boundary"]
    print(
        f"files={len(reports)} content={redaction} since={boundary['since'] or '-'} until={boundary['until'] or '-'}"
    )
    for row in output["usage"]:
        print(
            f"usage model={row['model']} effort={row['effort']} responses={row['responses']} input={row['input_tokens']} cached={row['cached_input_tokens']} output={row['output_tokens']} reasoning={row['reasoning_output_tokens']}"
        )
    for report in reports:
        calls = (
            ",".join(
                f"{name}:{count}" for name, count in sorted(report.tool_calls.items())
            )
            or "none"
        )
        yields = (
            ",".join(
                f"{value}:{count}"
                for value, count in sorted(report.wait_yield_ms.items())
            )
            or "none"
        )
        print(
            f"session={report.session} kind={report.kind} started={report.started_at or '-'} ended={report.ended_at or '-'} calls={calls} repeated_waits={report.repeated_waits} spawn_calls={report.spawn_calls} excess_spawn_calls={report.excess_spawn_calls} invalid_forks={report.invalid_forks} tool_failures={report.tool_failures} commands={report.command_executions} command_failures={report.command_failures} command_output_bytes={report.command_output_bytes} wait_yield_ms={yields} excess_cell_waits={report.excess_cell_waits} compactions={report.compactions} automatic_goal_continuations={report.automatic_goal_continuations} rapid_automatic_goal_continuations={report.rapid_automatic_goal_continuations} automatic_turns_without_change_events={report.automatic_turns_without_change_events} input_errors={report.input_errors}"
        )
        for detail in report.details:
            print(f"  {detail}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
