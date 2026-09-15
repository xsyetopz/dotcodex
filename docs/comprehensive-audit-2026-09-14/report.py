"""Produce traceable coverage and diagnostic totals, never billing estimates."""

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from analyze import FIELDS

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
REVIEWED = {
    24: "Guard inflation reported; commenter says other models also do this. No local causality established.",
    34: "60-second commentary complaint; screenshots and issue require separate verification.",
    40: "Premature stopping reported; goals, model changes and full access proposed without controlled proof. Do not weaken permissions.",
    50: "Mandatory wakeup claim conflates prompt guidance with timer behavior; screenshot unverified. Binary fork excluded by user.",
    55: "Observed partial sed reads on older models, not a universal 220-line loader limit. Contrary 700-line report retained.",
    59: "Image-heavy latency anecdote; smaller images helped one reporter, another reports no degradation. No local network causality established.",
    66: "Goal-loop anecdote; comments include successful goal blocking and questions. Universal inability to ask is not established.",
    114: "Reported controlled compressor comparison uses API prices, not Pro allowances. Linked results page fetch failed.",
    119: "Focused prompts and proportionate verification recommended; linked official article opened. No justification for deleting all skills.",
    126: "Higher effort sometimes finishes with more allowance left; task dependence and changing limits confound attribution. Cache claim unverified.",
    134: "Desktop/Remote inter-task regression; issue 40865 concerns 0.145/0.148. Not equivalent to CLI V2 sibling mail.",
    136: "Larger context versus experiment; alleged 2x subscription multiplier and guaranteed memory not established. Current catalog blocks experimental eligibility.",
    141: "V2 omitted fork_turns=all supported by source. Claimed 800k initial context and guaranteed cache miss not locally established; contrary comments retained.",
    155: "Parallelism cost question; contrary lower-token report uses Cline. Not a controlled Codex Pro comparison.",
}


def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + "\n")


def main():
    manifest = json.loads((OUT / "coverage.json").read_text())
    sessions = json.loads((OUT / "sessions.json").read_text())
    corpus_rows = sorted(
        (row for row in manifest["files"] if "/docs/reddit/" in row["path"]),
        key=lambda row: row["path"],
    )
    corpus = [Path(row["path"]) for row in corpus_rows]
    reviews = []
    links = {}
    for index, path in enumerate(corpus):
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != corpus_rows[index]["sha256"]:
            raise ValueError(f"Corpus changed after inventory: {path}")
        data = raw.decode()
        urls = re.findall(r"https?://[^\s<>]+", data)
        urls = sorted(set(url.rstrip(").,;\"'") for url in urls))
        reviews.append(
            {
                "path": str(path),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "disposition": "full local text reviewed"
                if index in REVIEWED
                else "not semantically reviewed",
                "finding": REVIEWED.get(index),
                "urls": urls,
            }
        )
        for url in urls:
            links.setdefault(url, []).append(str(path))
    write("corpus-review.json", reviews)
    write(
        "external-evidence.json",
        [
            {
                "url": url,
                "documents": paths,
                "disposition": "not individually verified; extraction may include incidental links",
            }
            for url, paths in sorted(links.items())
        ],
    )
    catalog = []
    path = ROOT / "docs/agent_engineering_problems_and_solutions.md"
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if "**" not in line:
            continue
        columns = line.split("|")
        catalog.append(
            {
                "line": number,
                "category": columns[1].strip(),
                "problem": columns[2].strip(),
                "solution": columns[3].strip(),
                "disposition": "problem and remedy read; local incident mapping and external citations pending",
            }
        )
    write("engineering-catalog.json", catalog)
    totals = {}
    for key in FIELDS:
        first = sum(x["usage"][0]["total"][key] for x in sessions if x.get("usage"))
        delta = sum(
            u["delta"][key]
            for x in sessions
            for u in x.get("usage", [])
            if u["delta"] is not None
        )
        final = sum(x["usage"][-1]["total"][key] for x in sessions if x.get("usage"))
        totals[key] = {
            "initial_counters": first,
            "observed_deltas": delta,
            "final_counters": final,
            "reconciles": first + delta == final,
        }
    ids = {x["metadata"][0]["id"] for x in sessions if x.get("metadata")}
    write(
        "historical-summary.json",
        {
            "files": len(sessions),
            "unreadable": sum("error" in x for x in sessions),
            "parse_errors": sum(len(x.get("errors", [])) for x in sessions),
            "duplicate_files": sum(x.get("duplicate_of") is not None for x in sessions),
            "trailing_partial_files": sum(
                x.get("trailing_partial_bytes", 0) > 0 for x in sessions
            ),
            "versions": dict(
                Counter(
                    m["cli_version"] for x in sessions for m in x.get("metadata", [])
                )
            ),
            "workers": sum(
                bool(x["metadata"][0]["parent_thread_id"])
                for x in sessions
                if x.get("metadata")
            ),
            "missing_parents": [
                m["parent_thread_id"]
                for x in sessions
                for m in x.get("metadata", [])
                if m["parent_thread_id"] and m["parent_thread_id"] not in ids
            ],
            "usage_events": sum(len(x.get("usage", [])) for x in sessions),
            "duplicate_cumulative": sum(
                u["duplicate_cumulative"] for x in sessions for u in x.get("usage", [])
            ),
            "resets": sum(u["reset"] for x in sessions for u in x.get("usage", [])),
            "nonduplicate_delta_last_mismatches": sum(
                u["delta_equals_last"] is False and not u["duplicate_cumulative"]
                for x in sessions
                for u in x.get("usage", [])
            ),
            "totals": totals,
            "warning": "Diagnostic counters only. Initial counters can contain inherited history. Cross-file replay and backend billing are not resolved.",
        },
    )
    cache_path = ROOT / "models_cache.json"
    raw = cache_path.read_bytes()
    cache = json.loads(raw)
    keys = [
        "slug",
        "context_window",
        "max_context_window",
        "effective_context_window_percent",
        "supports_experimental_context",
        "multi_agent_version",
        "multi_agent_reasoning_effort",
        "service_tiers",
    ]
    write(
        "catalog-observation.json",
        {
            "sha256": hashlib.sha256(raw).hexdigest(),
            "fetched_at": cache["fetched_at"],
            "client_version": cache["client_version"],
            "models": [{key: m.get(key) for key in keys} for m in cache["models"]],
        },
    )
    drift = []
    for row in manifest["files"]:
        if "sha256" not in row:
            continue
        path = Path(row["path"])
        try:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest != row["sha256"]:
                drift.append(
                    {"path": str(path), "before": row["sha256"], "after": digest}
                )
        except OSError as error:
            drift.append({"path": str(path), "error": type(error).__name__})
    write(
        "preservation-check.json",
        {
            "checked": len(manifest["files"]),
            "drift": drift,
            "excluded": "Native session/log/database/cache churn caused by the running harness; credentials not read",
        },
    )
    print(
        json.dumps(
            {
                "reviewed_documents": len(REVIEWED),
                "documents": len(corpus),
                "catalog_rows": len(catalog),
                "preservation_drift": len(drift),
            }
        )
    )


if __name__ == "__main__":
    main()
