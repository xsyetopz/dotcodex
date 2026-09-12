# Agent Routing

Choose the cheapest role that can reliably replace root work.

```mermaid
flowchart TD
    A[Substantial separable slice] --> B{Need code changes?}
    B -->|no| C{Hard architecture/root cause?}
    C -->|no| D[scout / docs / log analyst]
    C -->|yes| E[architect or hard debugger]
    B -->|yes| F{Mechanical or bounded?}
    F -->|yes| G[fast implementer / test engineer]
    F -->|no| H[implementer / UI engineer / debugger]
    E --> I[Return bounded result]
    D --> I
    G --> I
    H --> I
    I --> J[Root integrates]
```

Use reviewer after implementation when independent defect-finding is worth the
extra turn. Do not delegate merely to parallelize trivial work.

Never use Astra as a root coordinator.

Do not spawn for trivial work, tightly coupled steps, or tasks whose context
costs more to specify than the work itself. Do not use a reviewer as a
supervisor or a worker to wait on another worker. Prefer parallel children only
when their scopes and writes are independent; otherwise sequence them through
root integration.
