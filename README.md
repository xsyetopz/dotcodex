# Codex CLI 0.154.0 macOS suite

This repository is a raw `$CODEX_HOME` tree. Copy individual files manually.
It uses Codex's native model prompts and collaboration-mode instructions rather
than maintaining replacement prompts.

## Runtime policy

- Default: GPT-6 Astra Low; Plan Mode uses Medium reasoning.
- `coding`: GPT-5.6 Sol Medium.
- `fast-coding`: GPT-5.6 Luna High.
- `deep-coding`: GPT-6 Astra High.
- `security`: Daybreak Blue Medium.
- Standard service routing only; Fast mode is disabled.
- Low verbosity and reasoning summaries disabled.
- Stable goals, hooks, sleep, unified execution, and image inspection enabled.
- Experimental context management disabled.

Profiles inherit one concise developer policy from `config.toml`. They do not
set `model_instructions_file` or duplicate workflow instructions. Optional
profiles keep multi-agent execution disabled; the default profile exposes the
bounded role catalog.

The [GPT-6 Astra guidance][astra-guide] recommends concise instructions,
auditing skills and `AGENTS.md`, and specifying delegation and verification
behavior. This suite keeps those local deltas narrow and leaves tool contracts
to the pinned Codex client.

## Delegation

Singleton execution is the default. Delegation requires explicit authority and
is limited to one bounded worker plus, when independently justified, one
reviewer or debugger. The configured catalog contains six roles:

- `scout`: Luna High, read-only repository mapping.
- `docs_researcher`: Luna High, read-only primary-source research.
- `implementer`: Luna XHigh, bounded workspace edits.
- `debugger`: Sol Medium, reproduction and root-cause repair.
- `reviewer`: Sol Medium, independent read-only review.
- `cyber_defender`: Daybreak Blue Medium, authorized defensive analysis.

The spawn hook requires a configured role, rewrites accepted spawns to
`fork_turns="none"`, strips model and effort overrides, and rejects nested
spawning. One long, early-returning `wait_agent` window replaces status polling.
Subagents consume independent model and tool usage, so they are not a default
quota-saving mechanism; see the [Codex subagent guide][subagents].

## Instructions and skills

`AGENTS.md` is the durable engineering standard. Its numeric readability limits
are advisory review signals unless a repository defines its own limits.

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

## Compaction recovery

The compact hook stores a bounded original objective, latest user task state,
last assistant handoff, and Git status. Recovery data is:

- bound to the session, working directory, and transcript path;
- quoted and labeled as historical evidence;
- capped to the hook's 8,000-character context limit;
- consumed once;
- never authority or proof of completion.

Malformed, stale, or identity-mismatched checkpoints fail visibly and are
consumed or invalidated rather than replayed.

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
optional MCP services. No installer, migration script, or research snapshot is
included.

[astra-guide]: https://developers.openai.com/api/docs/guides/latest-model
[subagents]: https://learn.chatgpt.com/docs/agent-configuration/subagents
