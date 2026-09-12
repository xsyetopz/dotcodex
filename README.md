# Codex CLI 0.154.0 macOS suite

This is a raw `$CODEX_HOME` tree. Copy individual files manually.

Core layout:

- `model-instructions.md`: curated replacement for the bundled base prompt.
- `config.toml`: Sol Medium coordinator and named specialist registry.
- `AGENTS.md`: minimal cross-project guidance.
- `agents/*.toml`: role-specific prompt deltas only.
- `hooks/`: fresh-context spawn enforcement and compact continuity checkpoint.
- `skills/`: four custom packages with explicit invocation policy metadata.
- `*.config.toml`: optional root-model profiles.
- `scripts/`: CodeGraph/Headroom registration, health, and repository validation.
- `justfile`: pinned validation for skills, metadata, Markdown, Python, hooks, and
  Codex configuration.

Model routing:

- root: Sol Medium
- scout/docs: Luna Medium
- fast implementation/tests/logs: Luna High
- implementation/UI: Terra Medium
- debugger/reviewer: Terra High
- architecture: Astra Low
- exceptional diagnosis: Astra Medium
- authorized cyber/reversing: Daybreak Blue Medium

The suite intentionally avoids Sol High/XHigh/Max and Astra High/XHigh/Max as defaults.

Skill invocation boundaries:

- implicit: `execute-deterministic-workflow`, `operate-codex-goals`;
- explicit-only: `audit-codex-execution`, `orchestrate-codex-agents`.

Codex first loads each skill's name and description, then loads `SKILL.md` only
when routing selects or explicitly invokes it. Metadata alone can verify catalog
visibility and policy, but not model-selected implicit activation.

`codex debug prompt-input` verifies that the two implicit skills appear in the
catalog and the explicit-only skills do not. Its positional prompt is plain text
and does not create the TUI `text_elements` used for `$skill` mentions, so that
command alone cannot prove explicit package loading or model-selected routing.

Validate the suite:

```sh
just validate
```

Audit rollout signals without printing prompt or tool content:

```sh
python3 skills/audit-codex-execution/scripts/analyze_rollouts.py ~/.codex/sessions
```

CodeGraph 1.6.0:
`~/.codex/scripts/setup-codegraph.zsh`

Headroom:
`~/.codex/scripts/setup-headroom.zsh`

No installer or migration script is included.
