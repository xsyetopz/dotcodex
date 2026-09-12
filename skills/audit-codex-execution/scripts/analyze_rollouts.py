"""Analyze Codex rollout JSONL without exposing message or tool content by default."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import asdict, dataclass, field
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
    tool_calls: Counter[str] = field(default_factory=Counter)
    repeated_waits: int = 0
    invalid_forks: int = 0
    tool_failures: int = 0
    compactions: int = 0
    input_errors: int = 0
    details: list[str] = field(default_factory=list)

    def serializable(self) -> dict[str, Any]:
        result = asdict(self)
        result["tool_calls"] = dict(sorted(self.tool_calls.items()))
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
        if raw.get("isError") is True:
            return True
        exit_code = raw.get("exit_code")
        return isinstance(exit_code, int) and exit_code != 0
    if not isinstance(raw, str):
        return False
    try:
        decoded = json.loads(raw)
    except json.JSONDecodeError:
        return False
    return isinstance(decoded, dict) and (
        decoded.get("isError") is True
        or (isinstance(decoded.get("exit_code"), int) and decoded["exit_code"] != 0)
    )


def compact_event(event: dict[str, Any], payload: dict[str, Any]) -> bool:
    names = (event.get("type"), payload.get("type"))
    return any(isinstance(name, str) and "compact" in name.lower() for name in names)


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
    path: Path,
    aggregate: dict[tuple[str, str], Usage],
    include_content: bool = False,
) -> SessionReport:
    report = SessionReport(path.stem)
    models: dict[object, tuple[str, str]] = {}
    seen_usage: set[tuple[object, tuple[tuple[str, object], ...]]] = set()
    previous_wait = False
    current_model = ("?", "?")

    for event in iter_events(path, report):
        payload = event.get("payload")
        payload = payload if isinstance(payload, dict) else {}
        event_type = event.get("type")

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
                fork_turns = arguments.get("fork_turns") if arguments else None
                if fork_turns != "none":
                    report.invalid_forks += 1
            if include_content:
                rendered = (
                    json.dumps(arguments, sort_keys=True)
                    if arguments is not None
                    else "<unparsed>"
                )
                report.details.append(f"tool {short_name}: {rendered[:1000]}")
        if output_failed(payload):
            report.tool_failures += 1
            if include_content:
                report.details.append(
                    f"tool failure: {str(payload.get('output'))[:1000]}"
                )
        if compact_event(event, payload):
            report.compactions += 1

    return report


def rollout_files(root: Path, limit: int) -> list[Path]:
    try:
        files = list(root.rglob("rollout-*.jsonl")) if root.is_dir() else [root]
        return sorted(files, key=lambda path: path.stat().st_mtime, reverse=True)[
            :limit
        ]
    except OSError:
        return []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "sessions", nargs="?", type=Path, default=Path.home() / ".codex/sessions"
    )
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--include-content", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    aggregate: dict[tuple[str, str], Usage] = {}
    reports = [
        analyze_session(path, aggregate, args.include_content)
        for path in rollout_files(args.sessions, args.limit)
    ]
    output = {
        "content_redacted": not args.include_content,
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
    print(f"files={len(reports)} content={redaction}")
    for row in output["usage"]:
        print(
            "usage "
            f"model={row['model']} effort={row['effort']} responses={row['responses']} "
            f"input={row['input_tokens']} cached={row['cached_input_tokens']} "
            f"output={row['output_tokens']} reasoning={row['reasoning_output_tokens']}"
        )
    for report in reports:
        calls = (
            ",".join(
                f"{name}:{count}" for name, count in sorted(report.tool_calls.items())
            )
            or "none"
        )
        print(
            f"session={report.session} calls={calls} repeated_waits={report.repeated_waits} "
            f"invalid_forks={report.invalid_forks} tool_failures={report.tool_failures} "
            f"compactions={report.compactions} input_errors={report.input_errors}"
        )
        for detail in report.details:
            print(f"  {detail}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
