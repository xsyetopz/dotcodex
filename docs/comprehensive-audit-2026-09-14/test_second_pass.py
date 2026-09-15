import tempfile
import unittest
from pathlib import Path

from second_pass import capture


class InventoryTests(unittest.TestCase):
    def test_append_is_only_append_when_old_prefix_matches(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "session.jsonl"
            path.write_bytes(b"original\n")
            original = capture(path)
            self.assertEqual(capture(path, original)["change"], "unchanged")
            path.write_bytes(b"original\nappended\n")
            appended = capture(path, original)
            self.assertEqual(appended["change"], "appended")
            self.assertTrue(appended["previous_prefix_verified"])
            path.write_bytes(b"modified\nappended\n")
            self.assertEqual(capture(path, original)["change"], "changed")

    def test_partial_tail_is_not_in_complete_record_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "session.jsonl"
            path.write_bytes(b"complete\npartial")
            row = capture(path)
            self.assertEqual(row["bytes"], 16)
            self.assertEqual(row["complete_bytes"], 9)


if __name__ == "__main__":
    unittest.main()
