#!/usr/bin/env bun
/** Enforce named fresh-context MultiAgentV2 spawns. */

const ALLOWED = new Set([
	"architect",
	"cyber_defender",
	"debugger",
	"docs_researcher",
	"hard_debugger",
	"implementer",
	"implementer_fast",
	"log_analyst",
	"reverse_engineer",
	"reviewer",
	"scout",
	"test_engineer",
	"ui_engineer",
]);

function isObject(value) {
	return value !== null && typeof value === "object" && !Array.isArray(value);
}

function emit(payload) {
	process.stdout.write(`${JSON.stringify(payload)}\n`);
}

function deny(reason) {
	emit({
		hookSpecificOutput: {
			hookEventName: "PreToolUse",
			permissionDecision: "deny",
			permissionDecisionReason: reason,
		},
	});
}

function main(input) {
	let event;
	try {
		event = JSON.parse(input);
	} catch {
		deny("spawn_agent blocked: invalid hook input.");
		return;
	}

	if (!isObject(event)) {
		deny("spawn_agent blocked: hook input was not an object.");
		return;
	}

	const tool = String(event.tool_name ?? "").replaceAll("__", ".");
	if (tool !== "spawn_agent" && !tool.endsWith(".spawn_agent")) {
		return;
	}

	if (event.agent_id) {
		deny(
			"Nested subagent spawning is disabled; complete the delegated task directly.",
		);
		return;
	}

	if (!isObject(event.tool_input)) {
		deny("spawn_agent blocked: arguments were not an object.");
		return;
	}

	if (!ALLOWED.has(event.tool_input.agent_type)) {
		deny(`Select a configured agent_type: ${[...ALLOWED].sort().join(", ")}.`);
		return;
	}

	const updatedInput = { ...event.tool_input };
	delete updatedInput.fork_context;
	delete updatedInput.model;
	delete updatedInput.reasoning_effort;
	updatedInput.fork_turns = "none";

	emit({
		hookSpecificOutput: {
			hookEventName: "PreToolUse",
			permissionDecision: "allow",
			updatedInput,
		},
	});
}

main(await Bun.stdin.text());
