# Evidence-backed findings to date

## Role permission declarations do not restrict child permissions

**Classification: source-supported mechanism; local historical corroboration.**

Several local roles declare `sandbox_mode = "read-only"`; implementation roles
declare `workspace-write`. In pinned 0.154.0, `AgentRoleOverrides` does not
include permissions or sandbox settings. `apply_role_to_config_inner` projects
only selected fields into the inherited configuration. The upstream test
`apply_role_preserves_parent_sandbox_permissions` explicitly checks unchanged
parent permissions. Therefore a read-only role declaration is not a sandbox
boundary. The prose prohibition on edits remains a behavioral instruction.
[Role implementation][role], [permission test][role-test].

Historical corroboration: worker `01a0929c-e8b2-7723-8a82-bc9805bfb7f8`,
`session_meta` line 1, identifies parent
`01a091c2-d564-7d33-906e-85bd26865224` and `test_engineer`. Its `turn_context`
at line 8 records `danger-full-access`, despite today's role declaration of
`workspace-write`. This supports inherited permissions but does not establish
which role-file bytes existed then. No destructive incident is inferred.

**Candidate remedy:** document actual inheritance and use an appropriately
restricted parent execution boundary for tasks needing enforced read-only
access. Do not promise per-role sandbox isolation from these fields. Any
change must coordinate role files, descriptions, validators and documentation.

## Experimental-context opt-in does not establish activation

**Classification: source-supported eligibility; observed catalog mismatch.**

The local setting is `features.context_management.experimental_mode = true`.
Pinned `apply_experimental_context` additionally requires model capability,
eligible ChatGPT authentication/plan, compatible provider routing and successful
TokenBudget activation. Pro is eligible at the plan check, but that is only
one prerequisite. The observed 0.154.0 catalog advertises
`supports_experimental_context = false` for Astra, Sol, Terra and Luna.
This defeats that experimental activation path with that catalog; changing
the flag alone cannot repair it. [Eligibility implementation][context].

Counterevidence/limit: model-owned token-budget defaults are a separate path.
This finding does not prove every context mechanism is disabled, nor does a
cached catalog prove the live session used those exact bytes. No notes/history
or context-reset tools are exposed in this audit turn. Backend entitlement,
note durability and recovery benefits were not tested.

**Candidate remedy:** describe this as an inactive/conditional opt-in rather
than working memory. A capability override would be an unsupported experiment,
not discovery of upstream support. Do not falsify metadata or reset context on
the assumption that saving notes succeeded.

## V1 selection requires tracing precedence and retained thread metadata

**Classification: verified source behavior, not a V1 recommendation.**

For new selection, an enabled V2 feature explicitly selects V2. With V2 off,
`agents.enabled = false` explicitly disables agents. Otherwise the model's
catalog version precedes the legacy feature fallback. Thus enabling agents
and disabling V2 does not force V1 for a model advertising V2. Current cached
Astra/Sol/Terra entries advertise V2; Luna advertises V1.
[Configuration resolver][selection].

Existing thread metadata and inherited selections also participate. Old
resumed/forked threads without runtime metadata fall back to V1 in
`resolve_multi_agent_version`. A disk edit is not proof of a changed active
thread runtime. [Retained-thread resolver][retained].

V2's omitted/empty `fork_turns` defaults to `all`, and `fork_context` is
rejected. The local spawn hook rewrites accepted spawns to `none`, strips
model/effort overrides and rejects nested workers. Fixture behavior alone
does not establish every native delivery path. A V1 adoption must coordinate
this hook, instructions, tool names, waits and catalog handling rather than
only flipping a feature. [V2 parser][spawn].

## Service-tier strings and API prices do not prove subscription behavior

**Classification: verified local routing; backend accounting unknown.**

Pinned `get_service_tier` returns no explicit tier when `fast_mode` is false,
even if a string is schema-valid. With the gate enabled, non-default tiers
must be advertised by the model. The observed catalog lists priority, not
Flex. The current `service_tier = "default"`, `fast_mode = false` configuration
does not establish a working Flex route. [Tier resolver][tier].

No model-quality ranking, subscription multiplier or quota-saving promise
follows from that code. Subscription allowances, purchased credits and API
prices remain separate evidence domains.

## Historical accounting and analyzer limitations

**Classification: measured counters, not a billing ledger.**

All 171 inventoried files declare CLI 0.154.0. Fifty-one are children and every
parent identifier resolves to another inventoried file. Metadata `id` identifies
the thread; a child's `session_id` can identify its root session. The previous
analyzer prefers `session_id`, so it is not a valid unique thread key.

There are 13,545 usage observations, including 159 unchanged cumulative
snapshots, and no observed cumulative reset. Every nonduplicate consecutive
delta equals its reported last-response vector. Cached-input tokens are a
subset of input, and reasoning-output tokens a subset of output; do not add
either subset a second time.

| Counter | Initial counters | Observed deltas | Final counters |
| --- | ---: | ---: | ---: |
| Input | 44,093,371 | 1,491,079,767 | 1,535,173,138 |
| Cached input | 40,813,440 | 1,446,949,040 | 1,487,762,480 |
| Output | 161,846 | 5,351,908 | 5,513,754 |
| Reasoning output | 52,952 | 1,876,386 | 1,929,338 |

These are sums across file counters, **not unique account consumption**.
Three files begin with totals larger than their last-response usage; inherited
or earlier history must not be charged again. Exact file duplicates were not
found, but cross-file response replay still requires resolution. The previous
analyzer deduplicates by turn identifier plus last-usage values; equal-size
distinct responses can collide. The new fixture distinguishes that case.

The short worker above provides a reconciliation control: input responses
9,482 + 10,255 + 13,109 + 16,664 = 49,510. Cached-input responses sum to 39,936;
output responses sum to 3,197. Tool results corroborate creation of a bounded
local report; this is not proof that every recommendation inside it was right.

There are 8,379 canonical completed-command records, of which 1,010 have
failure status/nonzero exit. These are diagnostic signals, not 1,010 agent
defects. The historical data contains 309 changed rate-limit observations,
all labeled `pro`; this alone cannot establish the user's 20× tier or attribute
allowance changes to individual concurrent threads.

## A concrete short-wait loop, with a successful blocking control

In thread `01a0990e-5288-74e2-aeb2-4a50baddd640`, lines 3847, 3851 and
3855 request 10,000 ms waits on cell `549`. Each result says it is still
running and contains no new output. Line 3861 requests 300,000 ms; line 3863
reports completion after 222.5 seconds and a command session handle.

This supports avoidable short-wait round trips in that specific timeline.
It does not establish their exact quota charge. Multiple waits are not
inherently invalid when the preceding call remains running. The existing
300,000 ms cell-wait guidance addresses the observed behavior; a hard
one-wait-only ban would prevent legitimate continuation.

## Prompt policy, tools and contrary reports

Official guidance recommends task-specific skill routing and proportional
reading/testing, not deleting all skills. Local reports include both goal
looping and successful goal blocking, both image degradation and unaffected
long image sessions, and both expensive delegation and successful cheaper
parallel work in a different harness. None justifies a universal model rule.
[Official prompt guidance][guidance].

The current 4,000-token output policy is a readability/context tradeoff. This
audit encountered truncated combined reads and had to narrow them. Do not
mistake `cat` execution or a CodeGraph hit for receipt of the complete source.

The Desktop inter-task report concerns a different surface and records a
regression beginning before its runtime upgrade. It cannot establish a CLI V2
mail failure. [Original issue][desktop]. The compressor benchmark page returned
a web-tool `Internal Error`; its claims remain unverified. Claim-bearing
screenshots have not yet been visually inspected.

[role]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/agent/role.rs#L37-L132
[role-test]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/agent/role_tests.rs#L354-L391
[context]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/session/token_budget.rs
[selection]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/config/mod.rs#L1545-L1571
[retained]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/session/mod.rs#L468-L483
[spawn]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/tools/handlers/multi_agents_v2/spawn.rs#L290-L311
[tier]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/session/mod.rs#L984-L1013
[guidance]: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
[desktop]: https://github.com/openai/codex/issues/40865
