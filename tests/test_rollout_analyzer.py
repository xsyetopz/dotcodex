from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "skills/audit-codex-execution/scripts/analyze_rollouts.py"
SPEC = importlib.util.spec_from_file_location("analyze_rollouts", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
ANALYZER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ANALYZER
SPEC.loader.exec_module(ANALYZER)


class RolloutAnalyzerTests(unittest.TestCase):
    def test_reports_usage_waits_forks_failures_and_compaction_without_content(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            # Arrange
            rollout = Path(temporary_directory) / "rollout-test.jsonl"
            events = [
                {
                    "type": "turn_context",
                    "payload": {"turn_id": "t1", "model": "model", "effort": "medium"},
                },
                {
                    "type": "event_msg",
                    "payload": {
                        "type": "token_count",
                        "turn_id": "t1",
                        "info": {
                            "last_token_usage": {"input_tokens": 10, "output_tokens": 2}
                        },
                    },
                },
                {
                    "type": "response_item",
                    "payload": {
                        "type": "function_call",
                        "name": "spawn_agent",
                        "arguments": json.dumps(
                            {"fork_turns": "all", "message": "secret"}
                        ),
                    },
                },
                {
                    "type": "response_item",
                    "payload": {
                        "type": "function_call",
                        "name": "wait_agent",
                        "arguments": "{}",
                    },
                },
                {
                    "type": "response_item",
                    "payload": {
                        "type": "function_call",
                        "name": "wait_agent",
                        "arguments": "{}",
                    },
                },
                {
                    "type": "response_item",
                    "payload": {
                        "type": "function_call_output",
                        "output": json.dumps(
                            {"exit_code": 1, "output": "secret failure"}
                        ),
                    },
                },
                {"type": "compacted", "payload": {}},
            ]
            rollout.write_text(
                "".join(json.dumps(event) + "\n" for event in events) + "not-json\n"
            )
            aggregate: dict[tuple[str, str], Any] = {}

            # Act
            report = ANALYZER.analyze_session(rollout, aggregate)
            content_report = ANALYZER.analyze_session(rollout, {}, include_content=True)

            # Assert
            self.assertEqual(report.repeated_waits, 1)
            self.assertEqual(report.invalid_forks, 1)
            self.assertEqual(report.tool_failures, 1)
            self.assertEqual(report.compactions, 1)
            self.assertEqual(report.input_errors, 1)
            self.assertEqual(report.details, [])
            self.assertEqual(aggregate[("model", "medium")].input_tokens, 10)
            self.assertTrue(
                any("secret" in detail for detail in content_report.details)
            )


if __name__ == "__main__":
    unittest.main()
