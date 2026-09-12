# Token-Burn Avoidance

The expensive pattern is repeated inference over unchanged state.

Avoid:

```text
model -> status check -> model -> status check -> model -> status check
```

Prefer:

```text
model -> start work -> blocking runtime wait -> completion event -> model
```

Do not create a new inference turn merely to observe that a process or worker is
still running. Do not restart work because an observation timeout elapsed.
Do not duplicate worker work in the parent while waiting.

Use rollout auditing when a session shows high cached-input usage, repeated goal
continuations, or wait/status loops.

Common failure modes include restarting a process after an observation timeout,
running `get_goal` on every continuation, and completing a goal to escape a low
budget. Prefer durable handles, one blocking wait, and a completion audit
against the original objective.
