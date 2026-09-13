---
name: audit-codex-execution
description: >-
  Use only when explicitly invoked by name. Audit local Codex CLI rollouts and
  configuration for goal polling, wait loops, duplicated parent/worker work,
  full-history forks, tool failures, compaction churn, and avoidable token usage.
---

# Audit Codex Execution

Diagnose harness behavior from rollout evidence, not token totals alone.

Run the bundled standard-library analyzer. Its default report is
content-redacted:

```sh
python3 scripts/analyze_rollouts.py ~/.codex/sessions
python3 scripts/analyze_rollouts.py path/to/rollout.jsonl --json
```

Use `--include-content` only when the user authorizes inspection of prompts,
tool
arguments, and errors. Even then, report the minimum excerpt needed.

The analyzer reports aggregate model/effort usage and per-session tool counts,
repeated waits, non-fresh forks, failures, and compactions. Interpret these as
signals rather than verdicts. Parent/worker duplication and coordinator misuse
usually require authorized content inspection or comparison with worktree
evidence.

## Audit method

1. Select the smallest relevant rollout set and record its time/session
   boundary.
1. Run the redacted report before opening content.
1. Correlate anomalous sessions with config, prompts, hooks, or skill rules.
1. Separate measured counts from inferred causes.
1. Recommend one root-cause correction and a regression check.

Inspect for:

- goal continuations with no state-changing work;
- repeated `wait_agent` or shell status checks;
- huge repeated/cached input;
- parent work duplicating delegated work;
- spawned agents with `fork_turns` other than `none`;
- tool failures, including invalid timeout arguments;
- repeated compaction/recovery failures;
- expensive specialists acting as coordinators.

Do not use API pricing to estimate subscription quota consumption. Local token
events are diagnostic counters, not an authoritative billing ledger.

Trace each finding to the config, prompt, hook, or workflow rule that permits
it.
Recommend the smallest corrective change and distinguish measured evidence from
inference.

Read [audit signals](references/audit-signals.md).
