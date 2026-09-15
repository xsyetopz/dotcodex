# Codex 0.154.0 capability and reliability audit

## Result and provenance

The setup favors reliable completion and quota efficiency, not low latency.
Sol Medium remains the default; delegation is optional rather than compulsory.
Existing specialist models and effort levels remain available. No comparative
model trial establishes that replacing them would improve this user's work.

Audited on 2026-09-14 against installed `codex-cli 0.154.0` and a fresh clone of
[`openai/codex`, `rust-v0.154.0`][tag], commit
`6b9826e3aa83b1a5947db50f4332cb9c65f1b340`.

- Temporary audit root: `/tmp/codex-0154-audit.tTMmv1`.
- Source checkout: `upstream/` beneath that root.
- `codegraph init --yes` indexed 4,789 files, 150,601 nodes and 541,453 edges.
- Only `.codegraph/` was added to the upstream checkout; no upstream source
  files were changed or built.
- Both user repositories' tracked and untracked files were snapshotted before
  edits. Credentials, session stores, native databases and bundled system skills
  were excluded from the edit surface.

Read [research decisions](research.md) for conflicting claims and failure cases,
[corpus inventory](corpus.json) for all 166 original documents, and
[skill/resource dispositions](skills.json) for the complete package inventory.
Read [validation and rollback](validation.md) before activation or reversal.
These documents are task-specific reference material, not an always-loaded
prompt or a replacement for native goal state.

## What the source exposes

"Configured" means selected in this workspace, not proven usable by every
account, model, client, or turn. This execution's tool list is recorded in
[exposed tools](exposed-tools.json). No notes/history or agent collaboration
tools were exposed to this execution. That does not prove their absence from
Codex or from another profile.

| Surface | Source contract | Local disposition and limits |
| --- | --- | --- |
| Tool registration and exposure | [Core tool plan][tools] assembles utilities, execution, MCP, dynamic and extension tools; direct-only and code-mode exposure differ. | Treat the current turn's schema as authoritative. Internal handlers are not automatically callable. |
| Shell and long commands | Core execution tools register according to model, environment and feature selection. | `exec_command` and `write_stdin` are exposed. A command session ID is not a `functions.exec` cell ID. |
| Code mode | [Core tool plan][tools] selects executor and namespace exposure. | `functions.exec`/`functions.wait` are exposed. Direct-only tools must not be routed through nested calls. |
| Execution checklist | [Plan handler][plan] rejects Plan Mode independently of registration. | `tools.update_plan.enabled=true`; checklist updates do not switch collaboration modes. |
| Plan Mode and implementation UI | [Native Plan template][plan-template] supplies mode constraints; [TUI implementation][plan-ui] owns implementation actions. | Preserve native mode injection and complete `<proposed_plan>` blocks. Do not imitate UI state with prose. |
| Synchronous questions | [Core tool plan][tools] registers the handler with its allowed modes. | Default-mode availability is enabled. Optional clarification is not approval. |
| Asynchronous questions | [Core tool plan][tools] checks root status and advertised model tools. | Exposed here; do not assume the same interface on a child or another model. |
| Persisted goals | [Goal tools][goals] expose get/create/update with restricted status operations. | Enabled and exposed. Creation requires an explicit goal request. No agent tool for pause/resume or changing a goal budget is exposed by this spec. |
| Context experiment | [Eligibility and resolution][context] check model support, ChatGPT plan/auth, provider routes and feature permission. | Opt-in retained. Plus/Pro/ProLite appear in pinned client eligibility; official launch docs describe a narrower product rollout. Account/backend availability remains unverified. |
| Context reset | [Reset handler][reset] requests a new window without a save-success precondition; [rollover lifecycle][rollover] runs compaction hooks. | `new_context` is conditional on TokenBudget. The handler does not prove notes were saved, and resetting does not summarize old conversation history. |
| Remaining context | [Core tool plan][tools] registers `get_context_remaining` under TokenBudget. | Not exposed here. A context allowance is not a goal's lifetime token budget. |
| History and notes | [History/notes extension][notes] checks its configuration and backend authentication; tools call backend routes. | The public client is not the private service. Do not promise persistence, endpoint entitlement, cross-thread access or successful recovery from a flag alone. |
| Multi-agent V2 | The pinned baseline defaults omitted/empty `fork_turns` to `all`; V2 rejects `fork_context`. The `next/0.154.0` source fork changes omitted/blank input to fresh context. | V2 configured; V1 disabled. The local hook also rewrites accepted spawns to `none`; explicit source-fork `all` and positive counts remain available. |
| Agent lifecycle and mail | V2 handlers/specs implement spawn, messages, follow-up, interruption and waits. | Capability presence is not delegation authority. Mail and final-answer events are inputs to integration, not proof of correctness. |
| Sleep | [Core tool plan][tools] gates sleep by feature and mode/model support. | `always_on` configured; native sleep exposed. Avoid timed polling through model turns. |
| Hooks | [Hook runtime][hooks] supplies lifecycle events; [discovery][hook-trust] handles definition identity and trust. | Three existing user-scope entries retained. Script contents are not part of the definition hash; unchanged trust does not certify changed executable contents. |
| AGENTS.md | [Discovery][agents-md] applies byte limits and override/fallback precedence. | Shared constraints kept at the global root. Do not repeat all research or domain procedures there. |
| Skills | [Extension loading][skill-extension] and [host loading][skill-host] differ in main-prompt truncation. | Full details below. Metadata visibility does not prove selection, reading or application. |
| MCP resources | [Core tool plan][tools] registers list/read tools when MCP servers exist. | CodeGraph and Headroom retained. Resource availability and content quality must be checked from actual responses. |
| Web, media, apps and plugins | [Core tool plan][tools] plus extension/model capabilities determine availability. | Web and local image tools are exposed here; apps, image generation and plugins are disabled in user config. User preferences cannot manufacture missing tools. |
| Service tiers | [Session resolution][tiers] filters configured tiers; [protocol identifiers][tier-ids] define standard/Flex/Fast mapping. | `fast_mode=false` and `service_tier="default"`. The flag suppresses all explicit tiers, including Flex. No priority requests are intentionally selected. |
| Private backend behavior | The checkout includes client protocols and calls, not all server implementation. | Subscription quota accounting, entitlement decisions, remote note durability and server-side model behavior remain unknown. |

## Decisions implemented

### Completion and task ownership

The default agent can perform material work directly. A named specialist is an
option when it replaces root work, not a mandatory stage. Existing model
assignments remain a baseline, not a demonstrated optimum. The blanket claim
that Astra must never coordinate was removed from the general policy.

Instructions now distinguish verified completion from a checkpoint, promise,
or real blocker. Unfinished checklist entries must not be marked complete to
satisfy a final-answer rule. Native goals retain their own completion/blocked
rules. There is no new automatic goal creation, Stop-hook retry loop, governor,
or secondary goal database.

### Service policy

The pinned session resolver returns no explicit tier when fast mode is disabled.
It also rejects an unadvertised tier when the gate is enabled. The observed
catalog advertised `priority`, not `flex`, for Astra/Sol/Terra/Luna.
The protocol's explicit standard-routing sentinel is `default`; `standard` is
not that sentinel. This explains the difference between a schema accepting a
string and a working service selection.

The user's standard fallback is applied. `service_tier="default"` records that
intent, but is itself omitted by the disabled gate. No private-backend billing
or latency guarantee is inferred. The validator rejects fast mode or a
nonstandard tier in the base, retained profiles and named-role overrides.
Revisit Flex only after a version-matched source and catalog check; do not
silently enable fast mode to make it work.

### Continuity hook

The existing `PreCompact` / `SessionStart(source=compact)` checkpoint pair is
retained. Native rollover still uses compaction lifecycle hooks in this release;
the experiment does not make the pair automatically obsolete.

The checkpoint is supplemental evidence, not a complete task summary:

- Save invalidates previous evidence before replacement and uses an atomic
  rename with a private checkpoint file.
- Restore checks session, working directory and transcript identity, then
  consumes the checkpoint. Corrupt or mismatched evidence is not replayed.
- I/O and parsing failures are surfaced instead of silently succeeding.
  A missing checkpoint is expected absence, not successful recovery.
- Bounded excerpts are quoted, control delimiters escaped, and historical
  assistant/Git claims labeled as evidence rather than current authority.
- Existing bounds remain: a 4 MiB transcript tail and at most 8,000 characters
  of injected context. Older objectives can fall outside that tail.

The hook does not save native notes, certify a complete objective, prevent all
context loss, or guarantee progress. A failed hook can be nonblocking in the
provider lifecycle. Do not request `new_context` on the assumption that failed
note persistence or a best-effort checkpoint will recover the task.

### Skills and progressive disclosure

The pinned extension path caps main prompts at **8,000 UTF-8 bytes**. The legacy
host path applies that cap only to plugin skills; ordinary filesystem skills
there and direct file reads are not universally capped. The separate metadata
budget can shorten descriptions. None of this establishes a 220-line limit.

Five oversized entrypoints were reorganized without discarding their detailed
procedures: ASD-STE100, Apple documentation, duplication detection, duplication
refactoring, and Impeccable. Catalogs, detailed rules and maintenance routes now
have explicit loading conditions. This accommodates the constrained path; it
does not claim that every reference was executed or every behavior improved.

Four invalid frontmatters were repaired. Invocation policy belongs in
`agents/openai.yaml`, not portable frontmatter. Apple documentation and
find-skills now preserve their written explicit-only intent through that file;
the ADHD skill already had the correct client policy. `find-skills` remains
disabled in Codex configuration. Forbidden package-command examples were
corrected to Bun without changing detector algorithms or migration history.

Domain-specific resources were retained when their removal lacked evidence.
Unresolved indirect consumers, bundled executables and unexecuted host checks
are recorded per resource/package, not silently treated as passing audits.

[tag]: https://github.com/openai/codex/tree/rust-v0.154.0
[tools]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/tools/spec_plan.rs
[plan]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/tools/handlers/plan.rs
[plan-template]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/collaboration-mode-templates/templates/plan.md
[plan-ui]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/tui/src/chatwidget/plan_implementation.rs
[goals]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/ext/goal/src/spec.rs
[context]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/session/token_budget.rs
[reset]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/tools/handlers/new_context_window.rs
[rollover]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/compact_token_budget.rs
[notes]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/ext/history-notes/src/extension.rs
[spawn]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/tools/handlers/multi_agents_v2/spawn.rs
[hooks]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/hook_runtime.rs
[hook-trust]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/hooks/src/engine/discovery.rs
[agents-md]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/agents_md.rs
[skill-extension]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/ext/skills/src/extension.rs
[skill-host]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/ext/skills/src/host_prompt.rs
[tiers]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/session/mod.rs#L984-L1013
[tier-ids]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/protocol/src/config_types.rs#L527-L551
