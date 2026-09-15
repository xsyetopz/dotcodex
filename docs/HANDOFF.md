# Codex 0.154.0 reliability remediation

This document records the durable source, harness, validation, and rollback
boundaries for the audited Codex 0.154.0 work.

## Source identity and publication

- Harness repository: `/Users/krystian/.codex`.
- Harness branch: `audit/codex-0.154.0`.
- Source fork: `/Users/krystian/CodeProjects/xsyetopz/codex-next`.
- Source branch: `next/0.154.0`.
- Pinned upstream source: `6b9826e3aa83b1a5947db50f4332cb9c65f1b340`.
- Local package identity: `0.154.0-next`.
- Embedded CLI workspace identity: `codex-cli 0.154.0`.

No release, pull request, tag, history rewrite, Desktop replacement, or default
launcher activation is part of this work.

## Locally fixed behavior

The harness now uses one explicit execution path:

- Direct work is the default. Authorized delegation is bounded and fresh by
  default, with artifact-backed integration owned by the coordinator.
- Omitted or blank `fork_turns` is normalized to `none`; explicit `all` and
  positive counts remain intentional forks.
- `features.fast_mode` is explicitly `false`, and service routing uses the
  standard default sentinel.
- Goal completion and the three-consecutive-turn blocked audit use native goal
  state. Checkpoints supplement rather than replace that state.
- Compaction checkpoints are bounded and validated by schema, instance,
  integrity, and save-result checks before recovery is trusted.
- Waiting uses one blocking wait instead of repeated short polling.
- Completion claims require artifacts and verification evidence.

The rollout analyzer reports stopping, persistence, waiting, delegation,
recovery, and spawn fan-out signals. These are local detector measurements, not
subscription billing data or proof of model quality.

## Source-fork fixes

The pinned source fork contains additive changes for:

- V2 fresh-context defaults for omitted or whitespace-only `fork_turns`.
- Requested and resolved model and reasoning-effort metadata.
- Public metadata-only collaboration operation items without hidden reasoning,
  decrypted payloads, or new inference calls.
- Existing `SubAgentActivity` lifecycle items retained alongside collaboration
  operation items.
- One bounded activity projection shared by local `/subagents` and the
  daemon-wide `agents` overview.
- Replay and reconnect ordering and deduplication over live and loaded history.
- A disabled-by-default native `FastMode` feature.

The app-server change is additive. Unknown resolution data remains absent, and
older peers can ignore new optional fields. Full accessible transcript content
continues to use existing thread, turn, item, and timeline APIs.

## Mitigated behavior

Prompt and policy controls reduce premature stopping, repeated reviewer loops,
unbounded delegation, short polling, and unverifiable recovery. These controls
do not make model behavior deterministic and do not establish backend billing
or durability guarantees.

## External boundaries

This work does not claim to fix or expose:

- private backend persistence or entitlement behavior;
- subscription pricing, token accounting, or service eligibility;
- unavailable encrypted content or hidden reasoning;
- nondeterministic hosted-model behavior;
- Desktop-only rendering or host application behavior.

An anecdote or external report without a reproducer, failing test, or violated
source invariant did not trigger a product change. The finite decision record is
in `docs/comprehensive-audit-2026-09-14/control-matrix.md`.

## Validation and package

Harness validation is orchestrated by `just validate`. The source fork uses the
pinned Rust 1.95.0 toolchain and the repository-verified sandboxed V8 archive
and binding pair. Focused core, protocol, feature, and TUI checks run before the
complete `just test` suite. Unrelated pending snapshots are not accepted.

The package was assembled with the repository recipe under
`~/.local/state/codex-next/0.154.0-next/package`. Direct package-path checks
cover the CLI, helper binary, strict configuration doctor, app-server startup,
thread listing, and configuration reading. App-server smoke evidence confirms
that loaded configuration keeps Fast mode disabled. The installed Bun launcher
is checked before and after validation and is not replaced.

Generated app-server schemas and bindings come from the repository fixture
generator. The pinned `just write-app-server-schema` recipe names a missing
binary, so the direct repository script is the reproducible path until that
baseline recipe is repaired.

## Curated audit publication

Only files listed in
`docs/comprehensive-audit-2026-09-14/MANIFEST.sha256` are part of the curated
comprehensive-audit subset. It contains redacted conclusions, aggregate data,
reproduction scripts, a control matrix, and hashes. It excludes raw sessions,
downloaded media, external evidence payloads, credentials, logs, databases,
caches, Reddit captures, and operational directories.

## Rollback

1. Revert the scoped harness commit on `audit/codex-0.154.0` to remove local
   policy, hook, analyzer, validator, and publication changes.
1. Revert the scoped source-fork commit on `next/0.154.0` to remove protocol,
   core, TUI, schema, lockfile, feature-default, and documentation changes.
1. Do not reset either repository or overwrite unrelated work.
1. Delete the versioned local package only if it is no longer required as
   evidence. It is not active in the default launcher.
1. Rerun focused checks and `just validate`; start a fresh Codex session to load
   restored prompts and configuration.
