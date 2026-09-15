# Comprehensive audit publication

This directory contains the curated, redacted publication subset for the
Codex 0.154.0 harness audit. It records reproducible local controls and their
limits; it is not a statement about private billing, backend durability, or
nondeterministic model behavior.

## Coverage

- All 164 Reddit documents and 153 engineering-catalog rows were inventoried.
  Anecdotes without a reproducer, failing test, or violated invariant did not
  trigger product changes.
- All 171 files under `sessions/` accounted for and parsed at fixed per-file
  byte boundaries. `archived_sessions/` did not exist. No date cutoff,
  unreadable file, malformed record, exact duplicate or trailing partial record
  was encountered. This excludes unrelated backups outside Codex home.
- Configuration, role files, instructions, hooks, and both skill roots have
  fingerprints. Only evidence tied to the frozen control matrix is in the
  publication scope.
- External screenshots and claims remain contextual unless cited by a finding.
  The finite change set and its boundaries are in the
  [control matrix](control-matrix.md).

## Evidence files

| Artifact | Meaning |
| --- | --- |
| `coverage.json` | Original per-file boundaries, hashes and discovery inventory; never overwritten by the inventory script. |
| `historical-summary.json` | Reconciled diagnostic totals with accounting limitations. |
| `catalog-observation.json` | Versioned, hashed observation of model capability metadata. |
| `schema-check.json` | Global/profile schema checks and role-parser correction. |
| `preservation-check.json` | Comparison against 648 evidence-file fingerprints. |
| [Findings](findings.md) | Supported findings and explicit counterevidence. |
| [Decision log](decisions.md) | Candidate changes, risks and unresolved choices. |
| [Control matrix](control-matrix.md) | Reproducer-to-control mapping, compatibility, checks, and rollback. |
| `MANIFEST.sha256` | Integrity hashes for the explicitly published allowlist. |

## Source provenance

The existing source checkout remains at
`/tmp/codex-0154-audit.tTMmv1/upstream`.
Its HEAD is `6b9826e3aa83b1a5947db50f4332cb9c65f1b340`.
A fresh `git ls-remote` check returned the same peeled commit for
`rust-v0.154.0`; the annotated tag object is
`36eab01061df3cde5f95ec20a526777b430091ba`.
Tracked source is clean; its pre-existing `.codegraph/` is untracked.
CodeGraph was consulted before source navigation. Its local workspace index
reported stale files, so those files were read directly; it was not rebuilt.

## Validation and preservation

Six focused analyzer tests cover malformed records, missing metadata, equal
response sizes, duplicate cumulative events, resets, mixed versions/models,
parent/child identity and missing/reset limit windows.
Ruff checks and formatting pass for the audit scripts. All three audit Markdown
files pass the existing markdownlint configuration. Every JSON artifact parses.
The preservation comparison reports zero changes to 648 inventoried files.

Global config and all four profile overlays pass the pinned global JSON
schema. Raw role files fail that schema on `name` and `description`, as
expected: the upstream role parser removes metadata before config parsing.
All 13 role configuration bodies pass after that transformation. This does
not prove their settings take effect; the role permission finding illustrates
why the distinction matters.

The original read-only audit used an ephemeral validator environment. The
remediation subsequently runs the repository's full `just validate` workflow;
its final result is recorded in the implementation handoff.

Operational changes are separately reviewed in the repository diff and
validated by `just validate`. Audit outputs are not native memory or goal
state. The running harness can append sessions or refresh caches; those native
writes are excluded from publication and preservation claims.

## Reproduce

Run the audit script tests without reading private session payloads:

```console
python3 docs/comprehensive-audit-2026-09-14/test_analyze.py
python3 docs/comprehensive-audit-2026-09-14/test_second_pass.py
```

Run the harness analyzer tests and full repository validation from the root:

```console
python3 -m unittest tests.test_rollout_analyzer
just validate
```

The raw working evidence remains outside the publication allowlist. Never add
bulk sessions, downloaded media, raw external evidence, credentials, logs,
databases, caches, or operational directories to a commit.
