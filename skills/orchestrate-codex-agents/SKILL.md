---
name: orchestrate-codex-agents
description: >-
  Use only when explicitly invoked by name. Orchestrate Codex multi-agent v2 with
  bounded fresh-context handoffs, named specialist roles, non-overlapping work,
  mailbox-aware blocking waits, and root-owned integration.
---

# Orchestrate Codex Agents

This skill's invocation authorizes delegation for the requested task, but does
not require delegation when no useful independent slice exists. Keep the root as
the user-facing coordinator and final integration owner.

## Spawn

Use named roles and fresh context:

```json
{
  "task_name":"inspect_parser",
  "agent_type":"scout",
  "fork_turns":"none",
  "message":"Inspect parser ownership and call paths. Return findings only."
}
```

Use lowercase task names. Do not override model or reasoning effort. Use one
worker; add only a reviewer or debugger for independent verification or a
demonstrated failure. Give each child one bounded task with enough context to
work independently. Never ask a child to coordinate other agents.

All agents share the same worktree. Assign non-overlapping ownership to editing
workers, state that they are not alone in the repository, and tell them not to
revert concurrent edits.

## Mailbox lifecycle

- `send_message` adds context to a current turn and does not start a new one.
- `followup_task` starts a new turn on an idle existing child.
- `interrupt_agent` stops current work but keeps the child addressable.
- `list_agents` is for decisions that genuinely require live status.
- `FINAL_ANSWER` is delivered to the parent for review and integration.
- Collaboration tools are direct calls, not tools inside `functions.exec`.

Do not shadow delegated work. Continue independent root work while children run.
Use one blocking `wait_agent {}` only when a result blocks the next critical
step; never short-poll or spend a turn only checking status.

After completion, integrate, verify, and repair each child result. Do not
forward worker output unreviewed. Use the active profile's role and model
assignments; model names alone do not establish a coordination policy.

Read [routing](references/routing.md) for role selection and
[handoffs](references/handoffs.md) for task packet structure.
