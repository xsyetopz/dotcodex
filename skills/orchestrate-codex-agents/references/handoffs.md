# Handoffs

A child assignment should contain:

- objective;
- bounded scope;
- authoritative files/symbols when known;
- constraints that materially affect the answer;
- exact expected result;
- stop condition.

For editing work, also include exclusive file/module ownership and this shared-
worktree rule: other agents may edit concurrently; preserve their changes and do
not revert them. A fresh-context brief must include all task-specific facts the
child needs because `fork_turns:"none"` deliberately omits conversation history.

Good:

```text
Inspect src/parser and its callers for ownership of delimiter validation.
Return: current owner, duplicate checks, call path, and the smallest safe owner.
Do not edit files.
```

Bad:

```text
Look around the repo and improve the parser.
```

Use `fork_turns:"none"` so the handoff is explicit instead of duplicating the
parent's full conversation history.

## Integration packet

Expect the child to return changed paths or findings, verification performed,
and any unresolved risk. The root reviews the actual worktree and reruns the
smallest material integration check. A `FINAL_ANSWER` closes the child's current
turn; it does not close the root task.
