# Continuation Discipline

```mermaid
flowchart TD
    A[Goal continuation] --> B[Inspect authoritative current state]
    B --> C{2+ meaningful slices?}
    C -->|yes| D[update_plan]
    C -->|no| E[Execute next action]
    D --> E
    E --> F{State changed or useful evidence gained?}
    F -->|yes| G{Objective complete?}
    F -->|no| H{Known live wait?}
    H -->|yes| I[Block on native wait]
    H -->|no| J[Change approach or audit blocker]
    I --> G
    J --> K{Same blocker for 3 turns?}
    K -->|yes| L[update_goal blocked]
    K -->|no| E
    G -->|yes| M[Completion audit]
    G -->|no| E
    M --> N[update_goal complete]
```

Treat the worktree, process/job handles, tests, remote state, and current
artifacts as authoritative. Conversation history is navigation context, not
proof of completion.

## Continuation audit

Before ending a continuation, identify which authoritative state changed. If
none changed, the turn must have produced evidence that selects a different next
action, entered a blocking wait, or advanced the consecutive-blocker audit. A
goal status read, plan rewrite, or repeated diagnostic with identical output
does not qualify.

After a resumed blocked goal, reset the consecutive-blocker count. After
compaction, verify the checkpoint against current artifacts rather than
replaying completed actions.
