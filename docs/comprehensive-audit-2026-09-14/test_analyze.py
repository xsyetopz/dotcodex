import json
import unittest

from analyze import analyze


def record(kind, payload):
    return json.dumps({"type": kind, "payload": payload})


def usage(total, last):
    return record(
        "event_msg",
        {
            "type": "token_count",
            "info": {
                "total_token_usage": {"input_tokens": total},
                "last_token_usage": {"input_tokens": last},
            },
        },
    )


class AnalyzerTests(unittest.TestCase):
    def test_malformed_missing_metadata(self):
        result = analyze([b"{", b"null", usage(5, 5)])
        self.assertEqual(len(result["errors"]), 2)
        self.assertIsNone(result["usage"][0]["model"])
        self.assertIsNone(result["usage"][0]["delta"])

    def test_equal_response_sizes_are_not_duplicates(self):
        rows = analyze([usage(5, 5), usage(10, 5), usage(10, 5), usage(15, 5)])["usage"]
        self.assertEqual(
            [r["duplicate_cumulative"] for r in rows], [False, False, True, False]
        )
        self.assertEqual(
            sum(r["delta"]["input_tokens"] for r in rows if r["delta"]), 10
        )

    def test_reset_is_not_negative_usage(self):
        rows = analyze([usage(100, 5), usage(4, 4), usage(8, 4)])["usage"]
        self.assertTrue(rows[1]["reset"])
        self.assertIsNone(rows[1]["delta"])
        self.assertEqual(rows[2]["delta"]["input_tokens"], 4)

    def test_parent_and_thread_identity_are_distinct(self):
        result = analyze(
            [
                record(
                    "session_meta",
                    {
                        "id": "child",
                        "session_id": "root",
                        "parent_thread_id": "root",
                        "cli_version": "0.154.0",
                    },
                )
            ]
        )
        self.assertEqual(result["metadata"][0]["id"], "child")
        self.assertEqual(result["metadata"][0]["session_id"], "root")

    def test_mixed_versions_and_models_remain_visible(self):
        result = analyze(
            [
                record("session_meta", {"cli_version": "older"}),
                record(
                    "turn_context",
                    {"model": "one", "effort": "low", "multi_agent_version": "v1"},
                ),
                usage(4, 4),
                record("session_meta", {"cli_version": "0.154.0"}),
                record(
                    "turn_context",
                    {"model": "two", "effort": "high", "multi_agent_version": "v2"},
                ),
                usage(8, 4),
            ]
        )
        self.assertEqual([r["model"] for r in result["usage"]], ["one", "two"])
        self.assertEqual(len(result["metadata"]), 2)
        self.assertEqual(len(result["contexts"]), 2)

    def test_limits_preserve_reset_and_missing_windows(self):
        values = [
            {"primary": {"used_percent": 10, "resets_at": 1}},
            {"primary": {"used_percent": 0, "resets_at": 2}},
            {"primary": None},
        ]
        result = analyze(
            [
                record("event_msg", {"type": "token_count", "rate_limits": v})
                for v in values
            ]
        )
        self.assertEqual([r["value"] for r in result["limits"]], values)


if __name__ == "__main__":
    unittest.main()
