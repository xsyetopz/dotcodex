"""Freeze second-pass boundaries without replacing first-pass evidence."""

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

from inventory import OUT, ROOT, fingerprint

TARGET = OUT / "second-pass"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def capture(path, previous=None):
    row = fingerprint(path)
    with path.open("rb") as stream:
        data = stream.read(row["bytes"])
    after = fingerprint(path)
    if len(data) != row["bytes"] or any(
        row[key] != after[key] for key in ("device", "inode")
    ):
        raise OSError(f"File changed identity or shrank during capture: {path}")
    row["sha256"] = digest(data)
    row["complete_bytes"] = data.rfind(b"\n") + 1
    if previous is None:
        row["change"] = "added"
    else:
        row["previous_bytes"] = previous["bytes"]
        row["previous_sha256"] = previous["sha256"]
        prefix = data[: previous["bytes"]]
        row["previous_prefix_verified"] = (
            len(prefix) == previous["bytes"] and digest(prefix) == previous["sha256"]
        )
        row["change"] = (
            "unchanged"
            if row["sha256"] == previous["sha256"]
            else "appended"
            if row["previous_prefix_verified"]
            else "changed"
        )
    return row


def main():
    target = TARGET / "inventory.json"
    if target.exists():
        raise FileExistsError("Second-pass boundaries already exist")
    started = datetime.now(UTC).isoformat()
    baseline = json.loads((OUT / "coverage.json").read_text())
    sessions = json.loads((OUT / "sessions.json").read_text())
    old_files = {row["path"]: row for row in baseline["files"]}
    old_sessions = {row["path"]: row for row in sessions}
    paths = {Path(name) for name in old_files}
    for root in (
        ROOT / "docs/reddit",
        ROOT / "agents",
        ROOT / "hooks",
        ROOT / "model-instructions",
        ROOT / "skills",
        ROOT.parent / ".agents/skills",
    ):
        paths.update(
            path
            for path in root.rglob("*")
            if path.is_file() and not {".git", "__pycache__"}.intersection(path.parts)
        )
    paths.update(ROOT.glob("*.toml"))
    first_pass = sorted(path for path in OUT.iterdir() if path.is_file())
    session_paths = sorted(
        path
        for name in ("sessions", "archived_sessions")
        for path in (ROOT / name).rglob("*")
        if path.is_file()
    )
    result = {
        "started_at": started,
        "boundary": "Fixed per-file bytes; not an atomic filesystem snapshot",
        "first_pass": [capture(path) for path in first_pass],
        "files": [
            capture(path, old_files.get(str(path)))
            for path in sorted(paths)
            if path.is_file()
        ],
        "missing_files": sorted(name for name in old_files if not Path(name).exists()),
        "sessions": [
            capture(path, old_sessions.get(str(path))) for path in session_paths
        ],
        "missing_sessions": sorted(
            name for name in old_sessions if not Path(name).exists()
        ),
        "session_roots": {
            name: (ROOT / name).exists() for name in ("sessions", "archived_sessions")
        },
        "completed_at": datetime.now(UTC).isoformat(),
    }
    TARGET.mkdir(exist_ok=True)
    with target.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({key: len(result[key]) for key in ("files", "sessions")}))


if __name__ == "__main__":
    main()
