from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping

ROOT = Path(__file__).parents[1]


def run_hook(
    script: str, event: Mapping[str, object], home: Path | None = None
) -> dict[str, Any]:
    environment = os.environ.copy()
    if home is not None:
        environment["CODEX_HOME"] = str(home)
    result = subprocess.run(
        ["python3", str(ROOT / "hooks" / script)],
        input=json.dumps(event),
        text=True,
        capture_output=True,
        check=True,
        env=environment,
    )
    return json.loads(result.stdout) if result.stdout else {}


class SpawnPolicyTests(unittest.TestCase):
    def test_rewrites_accepted_spawn_to_fresh_context(self) -> None:
        # Arrange
        event = {
            "tool_name": "spawn_agent",
            "tool_input": {
                "task_name": "inspect",
                "agent_type": "scout",
                "fork_turns": "all",
                "model": "ignored",
            },
        }

        # Act
        output = run_hook("enforce_spawn_policy.py", event)

        # Assert
        hook = output["hookSpecificOutput"]
        self.assertEqual(hook["permissionDecision"], "allow")
        self.assertEqual(hook["updatedInput"]["fork_turns"], "none")
        self.assertNotIn("model", hook["updatedInput"])

    def test_denies_nested_spawn(self) -> None:
        # Arrange
        event = {
            "agent_id": "child",
            "tool_name": "spawn_agent",
            "tool_input": {"agent_type": "scout"},
        }

        # Act
        output = run_hook("enforce_spawn_policy.py", event)

        # Assert
        self.assertEqual(output["hookSpecificOutput"]["permissionDecision"], "deny")

    def test_denies_unknown_role(self) -> None:
        # Arrange
        event = {"tool_name": "spawn_agent", "tool_input": {"agent_type": "unknown"}}

        # Act
        output = run_hook("enforce_spawn_policy.py", event)

        # Assert
        self.assertEqual(output["hookSpecificOutput"]["permissionDecision"], "deny")


class CompactCheckpointTests(unittest.TestCase):
    def test_restores_saved_objective_after_compaction(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            # Arrange
            home = Path(temporary_directory)
            transcript = home / "rollout.jsonl"
            transcript.write_text(
                json.dumps(
                    {
                        "type": "response_item",
                        "payload": {
                            "type": "message",
                            "role": "user",
                            "content": [
                                {"type": "input_text", "text": "Finish the migration"}
                            ],
                        },
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            save_event = {
                "hook_event_name": "PreCompact",
                "session_id": "session-1",
                "transcript_path": str(transcript),
                "cwd": str(home),
            }

            # Act
            run_hook("compact_checkpoint.py", save_event, home)
            output = run_hook(
                "compact_checkpoint.py",
                {
                    "hook_event_name": "SessionStart",
                    "source": "compact",
                    "session_id": "session-1",
                },
                home,
            )

            # Assert
            context = output["hookSpecificOutput"]["additionalContext"]
            self.assertIn("Finish the migration", context)
            self.assertIn("Continue the active task", context)


if __name__ == "__main__":
    unittest.main()
