"""Read-only evidence inventory. Writes only explicitly selected audit artifacts."""

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent


def fingerprint(path):
    stat = path.stat()
    return {
        "path": str(path),
        "bytes": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
        "device": stat.st_dev,
        "inode": stat.st_ino,
    }


def main():
    target = OUT / "coverage.json"
    if target.exists():
        raise FileExistsError("Refusing to replace the original read boundaries")
    previous = json.loads((ROOT / "docs/audit-0.154.0/corpus.json").read_text())
    old = {str(ROOT / row["path"]): row["sha256"] for row in previous}
    corpus = sorted((ROOT / "docs/reddit").rglob("*"))
    corpus += [ROOT / "docs/agent_engineering_problems_and_solutions.md"]
    workspace = [ROOT / "AGENTS.md", ROOT / "hooks.json", ROOT / "justfile"]
    workspace += list(ROOT.glob("*.toml"))
    for directory in ["agents", "model-instructions", "hooks", "skills"]:
        workspace += list((ROOT / directory).rglob("*"))
    workspace += list((ROOT.parent / ".agents/skills").rglob("*"))
    rows = []
    for group, paths in [("corpus", corpus), ("workspace", workspace)]:
        for path in sorted(set(paths)):
            if not path.is_file() or any(
                x in path.parts for x in ["__pycache__", ".git"]
            ):
                continue
            row = {"group": group, **fingerprint(path)}
            try:
                data = path.read_bytes()
                row["sha256"] = hashlib.sha256(data).hexdigest()
                row["disposition"] = "inventoried; semantic review pending"
                if group == "corpus":
                    row["previous_audit"] = (
                        "unchanged"
                        if old.get(str(path)) == row["sha256"]
                        else "added"
                        if str(path) not in old
                        else "changed"
                    )
            except OSError as error:
                row["error"] = {"type": type(error).__name__, "message": str(error)}
            rows.append(row)
    sessions = []
    roots = []
    for name in ["sessions", "archived_sessions"]:
        directory = ROOT / name
        roots.append({"path": str(directory), "exists": directory.exists()})
        for path in sorted(directory.rglob("*")):
            if path.is_file():
                sessions.append({**fingerprint(path), "disposition": "pending"})
    target.write_text(
        json.dumps(
            {
                "created_at": datetime.now(UTC).isoformat(),
                "boundary": "Per-file byte lengths fixed at inventory; not an atomic snapshot",
                "session_roots": roots,
                "files": rows,
                "sessions": sessions,
            },
            indent=2,
        )
        + "\n"
    )
    print(json.dumps({"evidence_files": len(rows), "session_files": len(sessions)}))


if __name__ == "__main__":
    main()
