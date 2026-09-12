#!/usr/bin/env python3
"""Summarize recent rollout usage without printing prompt/tool content.

Diagnostic only; local counters are not an authoritative Pro billing ledger.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "sessions",
        nargs="?",
        default=str(Path.home() / ".codex" / "sessions"),
    )
    parser.add_argument("--limit", type=int, default=40)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    sessions = Path(args.sessions)

    try:
        files = sorted(
            sessions.rglob("rollout-*.jsonl"),
            key=lambda path: path.stat().st_mtime,
            reverse=True,
        )[: args.limit]
    except (FileNotFoundError, PermissionError, OSError):
        files = []

    rows: dict[tuple[str, str], list[int]] = defaultdict(lambda: [0, 0, 0, 0, 0])
    models: dict[object, tuple[str, str]] = {}
    seen: set[tuple[str, object, tuple[tuple[str, object], ...]]] = set()

    for path in files:
        try:
            handle = path.open(encoding="utf-8", errors="replace")
        except (FileNotFoundError, PermissionError, OSError):
            continue

        with handle:
            for line in handle:
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue

                payload = event.get("payload")
                if not isinstance(payload, dict):
                    continue

                if event.get("type") == "turn_context":
                    turn_id = payload.get("turn_id")
                    if turn_id is not None:
                        model = payload.get("model", "?")
                        effort = payload.get("effort", "?")
                        models[turn_id] = (str(model), str(effort))
                    continue

                if (
                    event.get("type") != "event_msg"
                    or payload.get("type") != "token_count"
                ):
                    continue

                info = payload.get("info")
                if not isinstance(info, dict):
                    continue

                usage = info.get("last_token_usage")
                if not isinstance(usage, dict) or not usage:
                    continue

                turn_id = payload.get("turn_id")
                key = (str(path), turn_id, tuple(sorted(usage.items())))
                if key in seen:
                    continue
                seen.add(key)

                row = rows[models.get(turn_id, ("?", "?"))]
                row[0] += 1
                row[1] += int(usage.get("input_tokens", 0) or 0)
                row[2] += int(usage.get("cached_input_tokens", 0) or 0)
                row[3] += int(usage.get("output_tokens", 0) or 0)
                row[4] += int(usage.get("reasoning_output_tokens", 0) or 0)

    print(f"files {len(files)}")
    for (model, effort), row in sorted(
        rows.items(),
        key=lambda item: item[1][1],
        reverse=True,
    ):
        print(
            f"{model:24} {effort:8} "
            f"responses={row[0]:5d} "
            f"input={row[1]:12d} "
            f"cached={row[2]:12d} "
            f"output={row[3]:9d} "
            f"reasoning={row[4]:9d}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
