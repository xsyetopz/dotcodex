# Codex CLI 0.154.0 macOS suite

This is a raw `$CODEX_HOME` tree. Copy individual files manually.

Core layout:

- `model-instructions.md`: curated replacement for the bundled base prompt.
- `config.toml`: Sol Medium coordinator and named specialist registry.
- `AGENTS.md`: minimal cross-project guidance.
- `agents/*.toml`: role-specific prompt deltas only.
- `hooks/`: fresh-context spawn enforcement and compact continuity checkpoint.
- `*.config.toml`: optional root-model profiles.
- `scripts/`: CodeGraph/Headroom registration, health, and usage diagnostics.

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

CodeGraph 1.6.0:
`~/.codex/scripts/setup-codegraph.zsh`

Headroom:
`~/.codex/scripts/setup-headroom.zsh`

No installer or migration script is included.
