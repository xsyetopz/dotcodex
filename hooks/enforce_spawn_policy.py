#!/usr/bin/env python3
"""Enforce named fresh-context MultiAgentV2 spawns."""

from __future__ import annotations

import json
import sys

ALLOWED = {
    "architect",
    "cyber_defender",
    "debugger",
    "docs_researcher",
    "hard_debugger",
    "implementer",
    "implementer_fast",
    "log_analyst",
    "reverse_engineer",
    "reviewer",
    "scout",
    "test_engineer",
    "ui_engineer",
}


def emit(payload: dict[str, object]) -> None:
    json.dump(payload, sys.stdout, separators=(",", ":"))
    sys.stdout.write("\n")


def deny(reason: str) -> int:
    emit(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }
    )
    return 0


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, TypeError, ValueError):
        return deny("spawn_agent blocked: invalid hook input.")

    if not isinstance(event, dict):
        return deny("spawn_agent blocked: hook input was not an object.")

    tool = str(event.get("tool_name", "")).replace("__", ".")
    if tool != "spawn_agent" and not tool.endswith(".spawn_agent"):
        return 0

    if event.get("agent_id"):
        return deny(
            "Nested subagent spawning is disabled; complete the delegated task directly."
        )

    tool_input = event.get("tool_input")
    if not isinstance(tool_input, dict):
        return deny("spawn_agent blocked: arguments were not an object.")

    role = tool_input.get("agent_type")
    if role not in ALLOWED:
        return deny(
            "Select a configured agent_type: " + ", ".join(sorted(ALLOWED)) + "."
        )

    updated = dict(tool_input)
    updated.pop("fork_context", None)
    updated.pop("model", None)
    updated.pop("reasoning_effort", None)
    updated["fork_turns"] = "none"

    emit(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "updatedInput": updated,
            }
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
