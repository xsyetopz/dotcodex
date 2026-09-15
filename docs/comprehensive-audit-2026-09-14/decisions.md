# Subsystem decision log

The remediation selects only directions supported by a reproducible defect or
implementation invariant. Other observations remain external boundaries.

| Subsystem | Selected direction | Alternative and maintenance/regression risk |
| --- | --- | --- |
| Permission inheritance | Correct read-only-role claims; enforce restrictions at the parent boundary. | Keep prose-only restrictions, explicitly accepting that they are not a sandbox. Changing parent permissions can block legitimate implementation. |
| V1/V2 coordination | Retain current behavior until version-specific evidence supports a change. | A version-checked catalog override may make V1 selectable, but requires coordinated hooks/tool consumers and upgrade review. No proven quality or quota advantage. |
| Context and recovery | Treat experimental activation as conditional; require actual exposed tools and successful persistence. | A reversible unsupported capability experiment remains a user choice, not upstream support. Backend failure could make a reset destructive. |
| Plans/goals/stopping | Keep explicit goals, native status and discriminating completion checks. | Automatic continuation might reduce handbacks but can loop, invent work or repeat blocked questions. No automatic goal creation proposed. |
| Models/effort/routing | Preserve baseline assignments pending workload evidence. | Higher/lower effort or specialized models may help individual tasks; no universal allowance benefit established. |
| Service tiers/usage | Preserve standard routing and separate diagnostic counters from billing. | Revisit Flex only after actual route eligibility; toggling fast mode can change routing and usage. |
| Instructions/skills | Remove demonstrated duplication or overbroad triggers only after consumer review. | Keep guidance that serves other models. Blanket deletion risks losing domain knowledge; larger routers increase repeated reads. |
| Shell/MCP/CodeGraph/output | Distinguish command sessions from execution cells; use current source after stale graph warnings. | Mandatory broad graph retrieval and small output caps can cause truncation/read churn. No index refresh or compression mandate proposed. |
| Images | Use sufficient resolution and focused captures where a task permits it. | Compression can erase deciding details. Session-file byte size is not network or quota proof. |
| Correctness/verification | Verify changed boundaries without unrelated test multiplication. | Static/fixture evidence cannot certify native hooks, backend tools or model adherence. |
| Toolchain policies | Consider a project-preserving exception to Bun-only, Xmake/Clang and no-Xcode rules. | Keeping global rules is simpler; exceptions add decision overhead but may avoid forced migrations or unverifiable platform builds. No policy changed; task-specific evidence still needed. |
| CodeGraph-first policy | Consider limiting mandatory graph use to structural/code-location questions where its index is useful. | Current rule already skips unindexed projects. Broader exceptions need clear wording to avoid bypassing useful dependency evidence. |

## Change requirements

Each change records the exact settings and affected subsystem, coordinated
consumers, supported versus experimental status, discriminating validation,
and scoped rollback in the control matrix. Restore only files whose current
hashes still match the implementation's recorded after-hashes, and preserve
intervening edits. Never restore credentials, caches, databases, or sessions.
