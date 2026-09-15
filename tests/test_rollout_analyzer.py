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
    def write_rollout(
        self, directory: Path, name: str, events: list[dict[str, Any]]
    ) -> Path:
        rollout = directory / name
        rollout.write_text(
            "".join(json.dumps(event) + "\n" for event in events), encoding="utf-8"
        )
        return rollout

    def test_reports_real_codex_events_without_content(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            rollout = self.write_rollout(
                Path(temporary_directory),
                "rollout-test.jsonl",
                [
                    {
                        "type": "session_meta",
                        "payload": {
                            "session_id": "worker-1",
                            "parent_thread_id": "root-1",
                            "timestamp": "2026-09-14T08:00:00Z",
                        },
                    },
                    {
                        "type": "turn_context",
                        "payload": {
                            "turn_id": "t1",
                            "model": "model",
                            "effort": "medium",
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "token_count",
                            "turn_id": "t1",
                            "info": {
                                "last_token_usage": {
                                    "input_tokens": 10,
                                    "output_tokens": 2,
                                }
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
                            "name": "spawn_agent",
                            "arguments": json.dumps({"fork_turns": "none"}),
                        },
                    },
                    {
                        "type": "response_item",
                        "payload": {
                            "type": "function_call",
                            "name": "spawn_agent",
                            "arguments": json.dumps({"fork_turns": "none"}),
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
                            "type": "function_call",
                            "name": "functions.wait",
                            "arguments": json.dumps(
                                {"cell_id": "cell-1", "yield_time_ms": 5000}
                            ),
                        },
                    },
                    {
                        "type": "response_item",
                        "payload": {
                            "type": "function_call",
                            "name": "functions.wait",
                            "arguments": json.dumps(
                                {"cell_id": "cell-1", "yield_time_ms": 5000}
                            ),
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "item_completed",
                            "turn_id": "t1",
                            "item": {
                                "type": "CommandExecution",
                                "status": "failed",
                                "exit_code": 1,
                                "aggregated_output": "secret command output",
                            },
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
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "task_complete",
                            "completed_at": 1789372860,
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "item_completed",
                            "item": {"type": "ContextCompaction"},
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "task_complete",
                            "completed_at": 1789372920,
                        },
                    },
                ],
            )
            aggregate: dict[tuple[str, str], Any] = {}
            report = ANALYZER.analyze_session(rollout, aggregate)
            content_report = ANALYZER.analyze_session(rollout, {}, include_content=True)
            self.assertEqual(
                (report.kind, report.started_at, report.ended_at),
                ("worker", "2026-09-14T08:00:00Z", "2026-09-14T08:02:00Z"),
            )
            self.assertEqual(
                (report.repeated_waits, report.invalid_forks, report.tool_failures),
                (1, 1, 2),
            )
            self.assertEqual((report.spawn_calls, report.excess_spawn_calls), (3, 1))
            self.assertEqual(
                (report.legacy_tool_failures, report.command_failures), (1, 1)
            )
            self.assertEqual(report.command_output_bytes, len(b"secret command output"))
            self.assertEqual(report.wait_cells, {"cell-1": 2})
            self.assertEqual(report.wait_yield_ms, {5000: 2})
            self.assertEqual((report.excess_cell_waits, report.compactions), (1, 1))
            self.assertEqual(report.details, [])
            self.assertEqual(aggregate[("model", "medium")].input_tokens, 10)
            self.assertTrue(
                any("secret" in detail for detail in content_report.details)
            )

    def test_selects_all_files_and_reports_automatic_signals(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            first = self.write_rollout(
                directory,
                "rollout-first.jsonl",
                [
                    {
                        "type": "session_meta",
                        "payload": {"timestamp": "2026-09-01T00:00:00Z"},
                    }
                ],
            )
            second = self.write_rollout(
                directory,
                "rollout-second.jsonl",
                [
                    {
                        "type": "session_meta",
                        "payload": {"timestamp": "2026-09-14T00:00:00Z"},
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "task_started",
                            "turn_id": "initial",
                            "started_at": 50,
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "task_complete",
                            "turn_id": "initial",
                            "completed_at": 100,
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "task_started",
                            "turn_id": "automatic",
                            "started_at": 150,
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "item_completed",
                            "turn_id": "automatic",
                            "item": {"type": "FileChange"},
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "task_complete",
                            "turn_id": "automatic",
                            "completed_at": 170,
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "item_completed",
                            "item": {"type": "UserMessage"},
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "task_started",
                            "turn_id": "user-turn",
                            "started_at": 180,
                        },
                    },
                ],
            )
            self.assertEqual(
                set(ANALYZER.rollout_files(directory, None)), {first, second}
            )
            since = ANALYZER.parse_boundary("2026-09-10T00:00:00Z")
            self.assertEqual(ANALYZER.rollout_files(directory, None, since), [second])
            report = ANALYZER.analyze_session(second, {})
            self.assertEqual(
                (
                    report.automatic_goal_continuations,
                    report.rapid_automatic_goal_continuations,
                    report.automatic_turns_without_change_events,
                ),
                (1, 1, 0),
            )


if __name__ == "__main__":
    unittest.main()
