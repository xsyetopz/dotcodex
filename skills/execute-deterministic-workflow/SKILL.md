---
name: execute-deterministic-workflow
description: >-
  Decompose and execute engineering work that has two or more meaningful slices,
  multiple deliverables, dependencies, or coherent validation milestones. Use
  Codex update_plan, deterministic batching, dependency sequencing, and evidence-
  based transitions. Do not use for one-step edits, advice-only questions, or
  Plan Mode deliverables.
---

# Execute Deterministic Workflow

Turn the requested outcome into executable slices before substantial work. This
skill governs execution planning; it does not enter or replace Plan Mode.

Use `update_plan` when there are at least two meaningful slices, multiple
deliverables, dependencies, or non-trivial goal work. Skip it only for genuinely
one-step tasks.

## Workflow

1. Derive concrete completion conditions from the request and current state.
1. Partition work by dependency and observable outcome.
1. Create the native Codex `update_plan` checklist when the tool is exposed.
1. Batch independent deterministic operations.
1. Execute dependent slices in order.
1. Update plan state when slices finish or evidence changes the path.
1. Validate at coherent milestones, then complete all plan steps.

Use this shape:

```json
{"plan":[
  {"step":"Inspect affected code","status":"in_progress"},
  {"step":"Implement scoped change","status":"pending"},
  {"step":"Run focused checks","status":"pending"}
]}
```

When evidence changes the path:

```json
{"explanation":"Observed failure changes the next action.","plan":[...]}
```

Statuses are only `pending`, `in_progress`, and `completed`; keep at most one
`in_progress`. Mark every step `completed` before final output.

## Transitions

- Complete a step only after its outcome exists or its evidence passes.
- Start the next dependency only after its prerequisite is complete.
- If evidence invalidates the path, replace affected future steps and explain
  why.
- If the tool is unavailable, retain the discipline without inventing textual
  native-plan state.
- In Plan Mode, follow the mode's read-only planning contract instead of this
  executable workflow.

Planning is not progress. Do not repeatedly rewrite the same plan or alternate
tiny edit/test cycles when one coherent batch can be validated. Delegation is
not
implied by a plan; it requires separate authorization and a slice that replaces
root work.

Read [workflow rules](references/workflow-rules.md) for slicing, batching,
milestones, and delegation handoff criteria.
