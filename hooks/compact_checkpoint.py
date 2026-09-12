#!/usr/bin/env python3
"""Minimal continuity checkpoint around remote compaction.

Codex 0.154.0's built-in OpenAI route uses remote compaction, so `compact_prompt`
is not relied on here. This hook saves only the latest visible task-state messages
plus git status and injects a bounded checkpoint on SessionStart(source=compact).
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

TAIL = 4 * 1024 * 1024
MSG_CAP = 6000
TOTAL_CAP = 12000


def home() -> Path:
    return Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))


def state_file(session_id: str) -> Path:
    directory = home() / "runtime" / "compact"
    directory.mkdir(parents=True, exist_ok=True)
    safe = "".join(char for char in session_id if char.isalnum() or char in "-_")
    return directory / f"{safe}.json"


def tail(path: str) -> list[str]:
    if not path:
        return []

    try:
        transcript = Path(path)
        size = transcript.stat().st_size
        with transcript.open("rb") as handle:
            if size > TAIL:
                handle.seek(size - TAIL)
                handle.readline()
            data = handle.read()
    except (FileNotFoundError, PermissionError, OSError):
        return []

    return data.decode("utf-8", "replace").splitlines()


def extract_text(content: object) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""

    parts: list[str] = []
    for item in content:
        if isinstance(item, dict):
            text = item.get("text")
            if isinstance(text, str):
                parts.append(text)
    return "\n".join(parts)


def recent(path: str) -> tuple[str, str]:
    user: str | None = None
    assistant: str | None = None

    for line in reversed(tail(path)):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue

        if event.get("type") != "response_item":
            continue

        payload = event.get("payload")
        if not isinstance(payload, dict) or payload.get("type") != "message":
            continue

        role = payload.get("role")
        text = extract_text(payload.get("content")).strip()
        if not text:
            continue

        if role == "assistant" and assistant is None:
            assistant = text[:MSG_CAP]
        elif role == "user" and user is None:
            user = text[:MSG_CAP]

        if user is not None and assistant is not None:
            break

    return user or "", assistant or ""


def git_state(cwd: str) -> str:
    if not cwd:
        return ""

    def run(*args: str) -> str:
        try:
            result = subprocess.run(
                ["git", "-C", cwd, *args],
                check=False,
                text=True,
                capture_output=True,
                timeout=3,
            )
        except (FileNotFoundError, PermissionError, subprocess.TimeoutExpired, OSError):
            return ""

        return result.stdout.strip() if result.returncode == 0 else ""

    branch = run("branch", "--show-current")
    head = run("rev-parse", "--short", "HEAD")
    status = run("status", "--short", "--untracked-files=normal")

    if not branch and not head and not status:
        return ""

    snapshot = f"branch={branch or '(detached)'} head={head or '?'}"
    if status:
        snapshot += "\n" + status[:3500]
    return snapshot


def save(event: dict[str, object]) -> None:
    session_id = str(event.get("session_id", ""))
    if not session_id:
        return

    transcript_path = event.get("transcript_path")
    user, assistant = recent(
        transcript_path if isinstance(transcript_path, str) else ""
    )

    cwd_value = event.get("cwd")
    cwd = cwd_value if isinstance(cwd_value, str) else "."

    data = {
        "user": user,
        "assistant": assistant,
        "git": git_state(cwd),
    }

    try:
        state_file(session_id).write_text(
            json.dumps(data, ensure_ascii=False),
            encoding="utf-8",
        )
    except (PermissionError, OSError):
        return


def restore(event: dict[str, object]) -> None:
    if event.get("source") != "compact":
        return

    session_id = str(event.get("session_id", ""))
    if not session_id:
        return

    try:
        data = json.loads(state_file(session_id).read_text(encoding="utf-8"))
    except (FileNotFoundError, PermissionError, OSError, json.JSONDecodeError):
        return

    if not isinstance(data, dict):
        return

    parts = [
        "<compact_recovery>",
        (
            "Continue the active task; do not start a new conversation or ask for "
            "a new task when the objective is recoverable."
        ),
    ]

    user = data.get("user")
    if isinstance(user, str) and user:
        parts.extend(("Latest user objective:", user))

    assistant = data.get("assistant")
    if isinstance(assistant, str) and assistant:
        parts.extend(("Last visible task state:", assistant))

    git = data.get("git")
    if isinstance(git, str) and git:
        parts.extend(("Current captured git state:", git))

    parts.extend(
        (
            (
                "Verify against the current worktree before editing; preserve "
                "existing completed work."
            ),
            "</compact_recovery>",
        )
    )

    text = "\n".join(parts)[-TOTAL_CAP:]
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": text,
            }
        },
        sys.stdout,
        separators=(",", ":"),
    )
    sys.stdout.write("\n")


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, TypeError, ValueError):
        return 0

    if not isinstance(event, dict):
        return 0

    hook_event = event.get("hook_event_name")
    if hook_event == "PreCompact":
        save(event)
    elif hook_event == "SessionStart":
        restore(event)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
