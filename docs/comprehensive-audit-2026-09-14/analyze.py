"""Analyze fixed rollout prefixes; no credentials, model calls or state writes."""

import hashlib
import json
from collections import Counter
from pathlib import Path

FIELDS = (
    "input_tokens",
    "cached_input_tokens",
    "cache_write_input_tokens",
    "output_tokens",
    "reasoning_output_tokens",
    "total_tokens",
)
OUT = Path(__file__).resolve().parent


def vector(value):
    if not isinstance(value, dict):
        return None
    if any(
        type(value.get(key, 0)) is not int or value.get(key, 0) < 0 for key in FIELDS
    ):
        return None
    return {key: value.get(key, 0) for key in FIELDS}


def analyze(records):
    result = {
        "metadata": [],
        "contexts": [],
        "usage": [],
        "limits": [],
        "errors": [],
        "events": Counter(),
        "tools": Counter(),
        "commands": {"completed": 0, "failed": 0},
        "waits": [],
    }
    previous = None
    current = {"model": None, "effort": None, "turn_id": None}
    seen_items = set()
    seen_contexts = set()
    for number, raw in enumerate(records, 1):
        try:
            event = json.loads(raw)
        except (json.JSONDecodeError, UnicodeDecodeError) as error:
            result["errors"].append({"line": number, "type": type(error).__name__})
            continue
        if not isinstance(event, dict) or not isinstance(event.get("payload"), dict):
            result["errors"].append({"line": number, "type": "InvalidRecordShape"})
            continue
        payload = event["payload"]
        kind = event.get("type")
        subtype = payload.get("type")
        stamp = {"line": number, "timestamp": event.get("timestamp")}
        result["events"][f"{kind}/{subtype}"] += 1
        if kind == "session_meta":
            keys = [
                "id",
                "session_id",
                "parent_thread_id",
                "timestamp",
                "cli_version",
                "source",
                "thread_source",
                "agent_role",
                "agent_path",
                "history_mode",
                "multi_agent_version",
                "context_window",
            ]
            result["metadata"].append(
                {**stamp, **{key: payload.get(key) for key in keys}}
            )
        if kind == "turn_context":
            current = {key: payload.get(key) for key in ["model", "effort", "turn_id"]}
            context = {
                key: payload.get(key)
                for key in [
                    "model",
                    "effort",
                    "multi_agent_version",
                    "approval_policy",
                    "sandbox_policy",
                ]
            }
            signature = json.dumps(context, sort_keys=True)
            if signature not in seen_contexts:
                seen_contexts.add(signature)
                result["contexts"].append({**stamp, **context})
        if kind == "event_msg" and subtype == "token_count":
            info = payload.get("info")
            if isinstance(info, dict):
                total = vector(info.get("total_token_usage"))
                last = vector(info.get("last_token_usage"))
                if total is not None:
                    duplicate = total == previous
                    reset = previous is not None and any(
                        total[k] < previous[k] for k in FIELDS
                    )
                    delta = (
                        None
                        if previous is None or reset
                        else {k: total[k] - previous[k] for k in FIELDS}
                    )
                    result["usage"].append(
                        {
                            **stamp,
                            **current,
                            "total": total,
                            "last": last,
                            "delta": delta,
                            "duplicate_cumulative": duplicate,
                            "reset": reset,
                            "delta_equals_last": delta == last
                            if delta is not None
                            else None,
                            "context_window": info.get("model_context_window"),
                        }
                    )
                    previous = total
                elif info.get("total_token_usage") is not None:
                    result["errors"].append({**stamp, "type": "InvalidUsageVector"})
            limits = payload.get("rate_limits")
            if limits is not None and (
                not result["limits"] or result["limits"][-1]["value"] != limits
            ):
                result["limits"].append({**stamp, "value": limits})
        if kind == "response_item" and subtype in {"function_call", "custom_tool_call"}:
            name = payload.get("name")
            if isinstance(name, str):
                result["tools"][name] += 1
                if name.rsplit(".", 1)[-1] in {
                    "wait",
                    "wait_agent",
                    "write_stdin",
                    "spawn_agent",
                }:
                    raw_args = payload.get("arguments", payload.get("input"))
                    try:
                        args = (
                            json.loads(raw_args)
                            if isinstance(raw_args, str)
                            else raw_args
                        )
                    except json.JSONDecodeError:
                        args = None
                    keys = [
                        "cell_id",
                        "session_id",
                        "yield_time_ms",
                        "timeout_ms",
                        "fork_turns",
                        "fork_context",
                        "agent_type",
                    ]
                    safe = (
                        {key: args[key] for key in keys if key in args}
                        if isinstance(args, dict)
                        else None
                    )
                    result["waits"].append(
                        {
                            **stamp,
                            "tool": name,
                            "call_id": payload.get("call_id"),
                            "arguments": safe,
                        }
                    )
        if kind == "event_msg" and subtype == "item_completed":
            item = payload.get("item")
            if isinstance(item, dict) and item.get("type") in {
                "CommandExecution",
                "command_execution",
            }:
                identity = (
                    payload.get("thread_id"),
                    payload.get("turn_id"),
                    item.get("id"),
                )
                if item.get("id") is not None and identity in seen_items:
                    continue
                seen_items.add(identity)
                result["commands"]["completed"] += 1
                if item.get("status") == "failed" or (
                    type(item.get("exit_code")) is int and item["exit_code"] != 0
                ):
                    result["commands"]["failed"] += 1
    result["events"] = dict(result["events"])
    result["tools"] = dict(result["tools"])
    return result


def read_prefix(row):
    path = Path(row["path"])
    with path.open("rb") as handle:
        data = handle.read(row["bytes"])
    if len(data) != row["bytes"]:
        raise OSError("Evidence file shrank below its fixed read boundary")
    stat = path.stat()
    if (stat.st_dev, stat.st_ino) != (row["device"], row["inode"]):
        raise OSError("Evidence file identity changed")
    complete = data.rfind(b"\n") + 1
    return data, complete


def main():
    manifest = json.loads((OUT / "coverage.json").read_text())
    reports = []
    hashes = {}
    for row in manifest["sessions"]:
        try:
            data, boundary = read_prefix(row)
            digest = hashlib.sha256(data).hexdigest()
            report = {
                "path": row["path"],
                "bytes": len(data),
                "complete_bytes": boundary,
                "trailing_partial_bytes": len(data) - boundary,
                "sha256": digest,
                "duplicate_of": hashes.get(digest),
            }
            hashes.setdefault(digest, row["path"])
            report.update(analyze(data[:boundary].splitlines()))
            report["disposition"] = (
                "fixed-prefix parsed; semantic timeline review pending"
            )
        except OSError as error:
            report = {
                "path": row["path"],
                "disposition": "unreadable",
                "error": {"type": type(error).__name__, "message": str(error)},
            }
        reports.append(report)
    (OUT / "sessions.json").write_text(json.dumps(reports, indent=2) + "\n")
    print(
        json.dumps(
            {
                "files": len(reports),
                "unreadable": sum("error" in r for r in reports),
                "parse_errors": sum(len(r.get("errors", [])) for r in reports),
            }
        )
    )


if __name__ == "__main__":
    main()
