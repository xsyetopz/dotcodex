# Validation, activation and rollback

## Baseline and executed checks

The baseline `just validate` failed on 26 line-length diagnostics in the
existing readability document. Separate baseline tests, Python checks and
doctor checks passed. Repairs preserved the document's meaning and retained
its original bytes in the backup; no lint rules were weakened.

| Check | Evidence and limits |
| --- | --- |
| Release provenance | `git ls-remote`, clone HEAD and annotated release agree on `6b9826e3aa83b1a5947db50f4332cb9c65f1b340`. |
| Source indexing | CodeGraph initialization succeeded; only its untracked index was added upstream. |
| `just validate` | Exit 0: skill validation, metadata, all retained profile prompt probes, Markdown, unit tests, Ruff, Pyright and whitespace checks pass. After the final optional-Git fix, focused validation reran all 24 unit tests, Ruff and Pyright. Doctor completed with the warning below. |
| Shared skill format | All 42 shared packages pass `skills-ref`; together with the four local packages, 46 packages pass. Four baseline frontmatter failures were repaired. |
| Hook subprocess fixtures | 14 tests pass, covering spawn policy, recovery, bounds, single use, identity mismatch, corrupt state, failed save, unavailable checkpoint directory, bounded transcript tails and recovery without Git. These are direct executions, not native lifecycle smoke tests. |
| Configuration tests | Eight tests pass, including rejection of priority/Fast/Flex/unrecognized-standard overrides and agent-role priority overrides under the selected fallback policy. |
| Shared hook assets | Three provider-fixture tests pass. They do not prove every provider's current hosted lifecycle. |
| ASD structural checker | `ste-lint.py --selftest` passes. It does not certify dictionary compliance or semantic preservation. |
| Just | Installed 1.58.0 matches the skill reference. Recipe listing, checker and actual validation recipe pass. |
| JavaScript formatting | Installed Biome formatted the changed hook. Bun executed it in synthetic temporary homes. No new JavaScript dependency was added. |
| Resource links | All 46 packages scanned for local inline/reference targets and client YAML parsed. The sole missing target is `CONTRIBUTING.md` in a README output template, where it is a destination-project link, not a missing bundled file. Anchors and all remote URLs are not certified by this check. |
| Profile loading | Base plus coding, fast-coding, deep-coding and security prompt probes passed. Plain prompt text does not prove explicit TUI skill activation or model-selected skill routing. |
| Endpoint health | The final doctor reports 21 OK, one idle, one warning and zero failures: macOS Gatekeeper diagnostics were unavailable for the desktop security assessment. Earlier runs reported 22 OK. HTTP and WebSocket checks passed; this is not notes/history entitlement or Flex support. |

Logs and the pre-edit snapshot are preserved outside the live repositories at:

`~/.local/state/codex-audits/2026-09-14-0.154.0-tTMmv1/`

The source checkout and working audit files remain at:

`/tmp/codex-0154-audit.tTMmv1/`

## Local rollout evidence

The existing redacted analyzer selected 133 rollout files whose session-start
timestamps fall between 2026-09-11T00:00:00Z and 2026-09-14T00:00:00Z.
It analyzes
whole selected files, including events after that upper boundary; these are
not event-window totals.

It reported 6,702 command executions, 838 command failures, 69 compactions,
290 automatic goal continuations, 234 automatic turns without recognized
change events, 104 excess cell waits, 38 spawn calls, 21 excess spawn-call
signals, zero invalid forks and zero input errors. These are detector signals,
not proven idle turns, unnecessary waits, or billable excess delegation.
Some valid mutations are not recognized as change events. Failed commands can
be useful diagnostics. No subscription billing or model-quality conclusion is
derived from these counters, and no prompt/tool content was included.

## Manual routing checks

| Package or boundary | Positive case | Nearest non-trigger or limitation |
| --- | --- | --- |
| execute-deterministic-workflow | Multi-slice execution with dependencies. | One edit, advice-only work, or externally selected Plan Mode. |
| operate-codex-goals | Explicit persisted goal or active goal continuation. | Ordinary task, a proposed goal prompt, or context-token allowance alone. |
| orchestrate-codex-agents | Explicit invocation with a useful independent task. | No-delegation authority or a simple direct task. |
| audit-codex-execution | Explicit request to diagnose rollout signals. | General coding or claims of exact subscription billing. |
| asd-ste100 | Ambiguous operational text requiring preserved meaning. | Creative copy or certified aerospace compliance. |
| axiom-apple-docs | Explicit Apple guide/diagnostic lookup. | A missing tool named `Read` or a supposed uninstalled session-start hook is not a prerequisite. |
| jscpd / dry-refactoring | Detection versus a requested refactor of confirmed clones. | Detection does not authorize edits; lookalikes need semantic review. |
| impeccable | Frontend design and the selected command playbook. | Backend work, unsolicited maintenance or hook installation. |
| find-skills | Explicit capability lookup when enabled. | Disabled in this Codex setup; metadata alone does not install anything. |
| i-have-adhd | Explicit output preference with current context. | Do not assume diagnosis or preference persistence in a new context. |
| maintain-agent-hooks | Lifecycle hook audit/change. | Git hooks or existing definition trust as proof of executable bytes. |
| maintain-agent-skills | Package and discovery audit. | AGENTS.md placement or arbitrary 220-line limits. |
| remove-legacy-compatibility | Removal after consumer retirement evidence. | Active migration or speculative cleanup. |
| write-justfiles | Existing orchestration recipes and actual installed version. | Reimplementing build logic in task recipes. |

These are manual distinctions, not observed model-selection trials. All
packages/resources have dispositions in `skills.json`: 14 changed, one reviewed
without changes, and 31 unresolved for full domain/reference or target-runtime
review. An unresolved package was preserved rather than deleted on weak
evidence. This audit does not certify every bundled executable or domain API.

An additional native catalog probe confirmed Apple documentation, find-skills
and the ADHD preference are not implicitly listed, while deterministic
workflow, goal operation and Impeccable remain listed. This verifies catalog
policy, not whether a model selects or correctly executes a skill.

## Activation and unavailable checks

- Start a fresh session to load changed prompt files, discovery metadata and
  configuration. Current loaded instructions are not retroactively replaced.
- On-disk defaults are not the current turn's permission contract. Doctor
  reported restricted defaults, while this execution received a separate
  full-access override. No sandbox or approval policy was changed.
- Review `hooks/compact_checkpoint.mjs` before relying on the next compaction.
  Its existing hook commands, events, matchers, timeouts and definition trust
  values were retained. No trusted hash was synthesized or approval bypassed.
- The provider hashes hook definitions, not script bytes. `/hooks` is the
  native review interface; changed definitions require its trust flow. Existing
  definition trust must not be presented as a script-content review.
- No new model session or agent was launched. Native hook event delivery,
  interactive trust review, compaction integration, backend note persistence,
  actual Flex handling and comparative model behavior were not executed.
- The checkpoint is a bounded supplement. It cannot recover an objective
  absent from its transcript tail, prove that a reported test passed, or replace
  the native goal/history/notes state. Failed persistence is not successful
  recovery.

## Scoped rollback

The durable backup contains `baseline/`, the original Git status/diffs,
`baseline-manifest.json`, and `changes.json` with before/after hashes for this
task's edits. It is a backup, not agent memory or native task state.

1. Close or pause affected sessions before a requested rollback. Compare each
   selected live file with its recorded after-hash. If it differs, preserve the
   newer work and merge the reversal instead of overwriting it.
1. Restore only selected changed files from `baseline/codex/` or
   `baseline/agents/`. These snapshots include pre-existing uncommitted work;
   do not substitute `git reset`, a checkout of HEAD, or a repository-wide copy.
1. Delete a task-added file only when its hash still matches `changes.json` and
   its consumers are reverted together. Restore split entrypoints and remove
   their new references as one coherent reversal.
1. For the hook, restore the prior script if required. Its configuration and
   trust entries were not changed by this task. Do not restore credentials,
   databases, sessions, logs, or unrelated project hook state.
1. Run relevant `just` checks and start a fresh session. Restoring the original
   readability document's formatting also restores its known baseline lint
   failures; do not hide that result.

The temporary source/index may be removed later independently of the backup.
Commit-addressed source links remain usable after temporary cleanup. Nothing
in this audit rewrote Git history or committed the user's existing changes.
