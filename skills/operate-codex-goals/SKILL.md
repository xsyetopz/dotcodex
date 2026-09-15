---
name: operate-codex-goals
description: >-
  Operate an explicitly requested or already-active persisted Codex goal through
  native goal tools, execution slices, authoritative-state checks, blocking waits,
  and strict completion or blocked audits. Do not create goals for ordinary tasks
  or use goal status as a substitute for doing work.
---

# Operate Codex Goals

Goals persist an objective across continuations. `update_plan` is only the
current
execution decomposition. Use both when appropriate.

Create a goal only when explicitly requested:

```json
create_goal {"objective":"Complete the requested migration."}
```

Add `token_budget` only when explicitly requested. Inspect state when the
objective, status, or remaining budget is not already authoritative:

```json
get_goal {}
```

Do not call `get_goal` merely to restate unchanged state. For any active goal
with two or more meaningful work slices, use `update_plan` before substantial
execution when available.

Each continuation must do one of these:

- change authoritative state;
- complete required work;
- obtain evidence that changes the next action;
- reach a valid terminal state.

A plan update or status restatement alone is not progress. After compaction or
resumption, reconcile goal state with the worktree, process handles, tests, and
artifacts. Conversation summaries guide navigation but do not prove completion.
Use native history and notes only when exposed. Before `new_context`, verify
that required recovery notes were saved successfully. The experimental flag
alone does not prove endpoint availability or successful persistence. A context
window token budget is not the goal's lifetime token budget.

## Waiting

Never burn goal continuations polling unchanged state. For a known live process,
job, or worker, use one blocking native wait or sleep. Resume reasoning when
state
can change or completion is reported.

## Completion

Mark complete only after current evidence proves every required objective item:

```json
update_goal {"status":"complete"}
```

Do not narrow the objective to match partial work. For a budgeted completed
goal,
report final token usage returned by the goal tool.

## Blocked

Use blocked only after the same real condition prevents meaningful progress for
at least three consecutive goal turns:

```json
update_goal {"status":"blocked"}
```

Hard, slow, uncertain, or incomplete work is not blocked. When a blocked goal is
resumed, start a fresh three-turn blocker audit. Never leave a terminal goal
active or mark it complete because its budget is nearly exhausted.

Read [continuation discipline](references/continuation-discipline.md) when
resuming, closing, or diagnosing a stalled goal. Read
[token-burn avoidance](references/token-burn.md) when repeated waits, context
reloads, or budget use impede progress.
