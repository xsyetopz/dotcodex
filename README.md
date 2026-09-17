# Codex CLI 0.154.0 macOS suite

This repository is a raw `$CODEX_HOME` tree. Copy individual files manually.
It uses Codex's native model prompts and collaboration-mode instructions rather
than maintaining replacement prompts.

## Runtime policy

- Default: GPT-6 Astra Medium; Plan Mode uses Medium reasoning.
- `coding`: GPT-5.6 Terra High.
- `fast-coding`: GPT-5.6 Luna High.
- `deep-coding`: GPT-6 Astra High.
- `security`: Daybreak Blue Medium.
- Standard service routing only; Fast mode is disabled.
- Low verbosity and reasoning summaries disabled.
- Stable goals, hooks, sleep, unified execution, and image inspection enabled.
- Experimental context management disabled.

Profiles inherit one concise developer policy from `config.toml`. They do not
set `model_instructions_file` or duplicate workflow instructions.
Coding profiles expose the bounded role catalog; security keeps its existing
direct-execution setting.

The [GPT-6 Astra guidance][astra-guide] recommends concise instructions,
auditing skills and `AGENTS.md`, and specifying delegation and verification
behavior. This suite keeps those local deltas narrow and leaves tool contracts
to the pinned Codex client.

Start difficult debugging goals with `codex --profile deep-coding`. There is no
automatic root-model switching. These choices are workload preferences, not a
measured performance ranking or a quota-saving guarantee.

`approvals_reviewer = "user"` explicitly disables automatic approval review
(Guardian). Sandbox and approval-policy settings are preserved.
`--approve-for-me` or an explicit configuration override can re-enable automatic
review for that invocation; avoid them when using this policy. Guardian is
separate from the optional Sol code-review role. See the
[configuration reference][config-reference].

## Delegation

Direct execution is normal. Optional delegation is authorized for substantial,
independent work, limited to one bounded worker plus one independently justified
reviewer or debugger. The configured catalog contains six roles:

- `scout`: Luna High, read-only repository mapping.
- `docs_researcher`: Luna High, read-only primary-source research.
- `implementer`: Terra High, bounded workspace edits.
- `debugger`: Astra High, difficult independent diagnosis and repair.
- `reviewer`: Sol High, read-only second opinions on concrete correctness risks.
  Excludes speculative improvements and style preferences.
- `cyber_defender`: Daybreak Blue Medium, authorized defensive analysis.

The spawn hook requires a configured role, rewrites accepted spawns to
`fork_turns="none"`, strips model and effort overrides, and rejects nested
spawning. One long, early-returning `wait_agent` window replaces status polling.
Subagents consume independent model and tool usage, so they are not a default
quota-saving mechanism; see the [Codex subagent guide][subagents].

## Instructions and skills

`AGENTS.md` holds engineering preferences and toolchains. Execution policy lives
in `config.toml`; role files contain role-specific responsibilities. The brief
delegation authorization in `AGENTS.md` satisfies native Codex authority checks;
the limits remain in configuration. Global
numerical complexity thresholds are removed; repository requirements and actual
readability problems guide review.

The custom skill set is intentionally small:

- implicit: `operate-codex-goals`;
- explicit-only: `orchestrate-codex-agents`, `audit-codex-execution`.

The multi-slice checklist rule lives in `config.toml`; it does not require a
separate workflow skill. Each retained skill keeps operational detail in its
`references/` directory.

CodeGraph and Headroom remain available. Use CodeGraph for a concrete
cross-file structural question and Headroom for a concrete large-output
reduction need. Availability alone does not prove either tool reduces token
usage.

## Context recovery

The existing checkpoint hook handles `Stop`, `PreCompact`, and `SessionStart`.
It makes no model calls. Private artifacts live at
`$CODEX_HOME/runtime/compact/<workspace-sha256>/<session-id>.json`,
with directory
mode 0700 and file mode 0600. Session and working-directory identity keep
concurrent sessions and worktrees separate.

- `Stop` saves end-of-turn evidence and the complete latest
  `<proposed_plan>` in a separate `.json.plan.md` file. Transcript scanning is
  streamed without a tail cap, so long plans are not silently truncated.
- `PreCompact` checkpoints evidence and creates a pending-injection marker.
- `SessionStart(source=compact)` injects at most 8,000 characters of quoted
  recovery evidence and artifact pointers. After manual compaction, Codex runs
  this hook at the next turn. It consumes only the marker.
- `SessionStart(source=startup|clear)` offers up to five matching workspace
  pointers. It does not inject old task content, select the newest file as
  authoritative, or resume old work automatically.

The hook captures bounded original/latest user excerpts, the latest assistant
message, Git status, and semantic notes when present. At meaningful milestones
in substantial work, the agent writes compact notes from the session working
directory using the existing handler:

```sh
bun --no-env-file --no-install \
  "${CODEX_HOME:-$HOME/.codex}/hooks/compact_checkpoint.mjs" notes <<'JSON'
{
  "objective": "Fix the parser",
  "constraints": "Preserve the public API",
  "completed": "Reproduced the failure",
  "verification": "Focused parser test failed, exit 1",
  "failed_approaches": "Increasing the timeout did not help",
  "blockers": "none",
  "next_action": "Correct token handling"
}
JSON
```

The command uses the native `CODEX_THREAD_ID` and writes `.json.notes.json`.
All seven fields are strings; use `unknown` for missing evidence. Notes are
limited to 16,000 characters and preserved by hooks, not regenerated after each
tool call. Raw transcript excerpts are not proof of completed work.

A newly supplied request and implementation plan remain authoritative. Missing,
malformed, identity-mismatched, or older-than-seven-days checkpoints report
diagnostics without replaying stale state. A failed save retains old artifacts
for inspection, removes pending injection, and marks the failure. Missing Git
only omits the Git snapshot with a diagnostic. Hook failures never request an
automatic continuation. Transcript parsing targets the installed 0.154.0 format,
which is not a stable public interface; see the [hook contract][hooks].

Review changed definitions using `/hooks` (or its native `hooks/list` and
`config/batchWrite` trust flow). Unreviewed definitions are skipped by Codex.
Do not bypass hook trust.

Rollback only the changed configuration, profiles, instructions, roles, handler,
and hook entries, including their specific trust records. Preserve other hook
entries, the Reddit corpus, and private runtime artifacts.

## Validation

Run the complete suite:

```sh
just validate
```

The harness validator checks the pinned `codex-cli 0.154.0` binary, model and
profile routing, six roles, two-child ceiling, three-skill policy, stable
feature states, and native prompt composition. It runs `codex debug
prompt-input` for the base configuration and every profile, requiring one
developer policy, one `AGENTS.md` payload, one skill catalog, and no removed
workflow instruction.

Focused commands:

```sh
just harness
just tests
just doctor
python3 skills/audit-codex-execution/scripts/analyze_rollouts.py \
  ~/.codex/sessions --limit 5
```

`scripts/setup-codegraph.zsh` and `scripts/setup-headroom.zsh` configure the
optional MCP services. Research under `reddit-codex/` is preserved and does not
establish subscription savings.

[astra-guide]: https://developers.openai.com/api/docs/guides/latest-model
[subagents]: https://learn.chatgpt.com/docs/agent-configuration/subagents

[config-reference]: https://learn.chatgpt.com/docs/config-file/config-reference
[hooks]: https://learn.chatgpt.com/docs/hooks
