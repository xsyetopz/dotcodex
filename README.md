# Codex CLI 0.154.0 macOS suite

This is a raw `$CODEX_HOME` tree. Copy individual files manually.

Core layout:

- `model-instructions/`: complete model-specific replacements for the bundled
  base prompt.
- `config.toml`: Sol Medium task owner and optional named specialists.
- `AGENTS.md`: minimal cross-project guidance.
- `agents/*.toml`: role-specific prompt deltas only.
- `hooks/`: fresh-context spawn enforcement and compact continuity checkpoint.
- `skills/`: four custom packages with explicit invocation policy metadata.
- `*.config.toml`: optional root-model profiles.
- `scripts/`: CodeGraph/Headroom registration, health, and repository
  validation.
- `justfile`: pinned validation for skills, metadata, Markdown, Python, Bun
  hooks, and Codex configuration.

Lifecycle hooks are dependency-free `.mjs` modules run by Bun 1.4.2 with
workspace environment-file loading and package auto-installation disabled.

Model routing:

- root: Sol Medium
- scout/docs: Luna Medium
- fast implementation/tests/logs: Luna High
- implementation/UI: Terra Medium
- debugger/reviewer: Terra High
- architecture: Astra Low
- exceptional diagnosis: Astra Medium
- authorized cyber/reversing: Daybreak Blue Medium

Harness prompt routing:

- base / GPT-5.6 Sol: `model-instructions/sol.md`
- coding / GPT-5.6 Terra: `model-instructions/terra.md`
- fast-coding / GPT-5.6 Luna: `model-instructions/luna.md`
- deep-coding / GPT-6 Astra: `model-instructions/astra.md`
- security / Daybreak Blue: `model-instructions/sol.md`

Every profile sets `model_instructions_file` explicitly. Daybreak Blue reuses
the Sol contract because the current alias resolves to GPT-5.6 Sol, while its
defensive scope remains in `security.config.toml`.

The suite intentionally avoids Sol High/XHigh/Max and Astra High/XHigh/Max as
defaults.

Reliability and quota efficiency take precedence over latency. Work directly
unless an independent slice benefits from a specialist. Keep
`features.fast_mode=false`; standard service is the authorized fallback.
In the pinned client this flag suppresses every explicit tier, including Flex.
`service_tier="default"` records standard intent; `standard` is not its wire
identifier. The validator checks base/profile/role overrides for this policy.

The [source audit](docs/audit-0.154.0/README.md) maps native capabilities,
conditional features, research conflicts, and all user-owned skill resources.
It also documents checkpoint limitations, activation and scoped rollback.
The checkpoint supplies single-use, quoted historical evidence, not a complete
objective or authoritative native goal state. Review changed hook scripts;
their contents are not covered by the hook definition's trusted hash.

Skill invocation boundaries:

- implicit: `execute-deterministic-workflow`, `operate-codex-goals`;
- explicit-only: `audit-codex-execution`, `orchestrate-codex-agents`.

Codex first loads each skill's name and description, then loads `SKILL.md` only
when routing selects or explicitly invokes it. Metadata alone can verify catalog
visibility and policy, but not model-selected implicit activation.

The harness validator runs `codex debug prompt-input` against the base
configuration and every profile. It verifies each profile's developer
instructions, `AGENTS.md`, the sentinel user prompt, and that the two implicit
skills appear in the catalog while the explicit-only skills do not. Its
positional prompt is plain text and does not create the TUI `text_elements` used
for `$skill` mentions, so the probe cannot prove explicit package loading or
model-selected routing.

## Harness contract provenance

The suite is pinned to `codex-cli 0.154.0`. Each file in
`model-instructions/` is a complete replacement under the
[Codex configuration contract][config-reference]. The prompts share only the
hard harness contract and vary their model-specific execution stance. Native
collaboration instructions remain enabled so Plan and Default mode behavior
comes from Codex.

Every model prompt follows the [GPT-5.5 suggested prompt structure][gpt-5-5]:
`Role` → `Personality` → `Goal` → `Success criteria` → `Constraints` →
`Output` → `Stop rules`. The Sol, Terra, and Luna content applies the
[GPT-5.6 guidance][gpt-5-6] through outcome-first instructions, explicit
autonomy boundaries, and concise tool rules. Astra keeps the same structural
baseline but is materially shorter, following the
[Astra prompt guidance][astra-prompt-guidance] to avoid process-heavy
instructions that can overconstrain the model. The
[Daybreak Blue model entry][daybreak-blue] identifies its current snapshot as
GPT-5.6 Sol.

The reference audit used the upstream `openai/codex` source at tag
[`rust-v0.154.0`][source-tag], commit
[`6b9826e3aa83b1a5947db50f4332cb9c65f1b340`][source-commit].
The inspected contract points were:

- the [Plan collaboration template][plan-template],
  which separates Plan Mode from `update_plan` and requires
  `<proposed_plan>`;
- the [`update_plan` handler][plan-handler],
  which rejects checklist updates in Plan Mode;
- the [tool registration path][tool-registration],
  which registers the handler only when `update_plan_enabled` is true;
- the [Plan implementation UI][plan-implementation],
  which turns a Plan item into stay-in-Plan, implement, and clear-context
  implementation actions.

Before changing the pinned CLI version:

1. Re-audit those four source paths and the proposed-plan stream parser.
1. Confirm configuration keys, tool schemas, collaboration-mode injection, and
   feature states against the new binary.
1. Update the version, source tag, commit, validator expectations, and harness
   instructions together.
1. Run every base/profile prompt probe and the complete `just validate` suite.

Validate the suite:

```sh
just validate
```

Audit rollout signals without printing prompt or tool content:

```sh
python3 skills/audit-codex-execution/scripts/analyze_rollouts.py \
  ~/.codex/sessions
```

CodeGraph 1.6.0:
`~/.codex/scripts/setup-codegraph.zsh`

Headroom:
`~/.codex/scripts/setup-headroom.zsh`

No installer or migration script is included.

[config-reference]: https://learn.chatgpt.com/docs/config-file/config-reference
[astra-prompt-guidance]: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
[daybreak-blue]: https://developers.openai.com/api/docs/models/gpt-daybreak-blue-latest
[gpt-5-5]: https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.5
[gpt-5-6]: https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.6
[plan-handler]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/tools/handlers/plan.rs
[plan-implementation]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/tui/src/chatwidget/plan_implementation.rs
[plan-template]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/collaboration-mode-templates/templates/plan.md
[source-commit]: https://github.com/openai/codex/commit/6b9826e3aa83b1a5947db50f4332cb9c65f1b340
[source-tag]: https://github.com/openai/codex/tree/rust-v0.154.0
[tool-registration]: https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/tools/spec_plan.rs
