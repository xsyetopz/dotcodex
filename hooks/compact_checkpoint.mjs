#!/usr/bin/env bun

/**
 * Minimal continuity checkpoint around remote compaction.
 *
 * Codex 0.154.0's built-in OpenAI route uses remote compaction, so
 * `compact_prompt` is not relied on here. This hook saves only the latest
 * visible task-state messages plus git status and injects a bounded checkpoint
 * on SessionStart(source=compact).
 */

import { spawnSync } from "node:child_process";
import {
	closeSync,
	fstatSync,
	mkdirSync,
	openSync,
	readFileSync,
	readSync,
	writeFileSync,
} from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";

const TAIL = 4 * 1024 * 1024;
const MESSAGE_CAP = 6000;
const TOTAL_CAP = 12000;

function isObject(value) {
	return value !== null && typeof value === "object" && !Array.isArray(value);
}

function limitStart(text, length) {
	return [...text].slice(0, length).join("");
}

function limitEnd(text, length) {
	return [...text].slice(-length).join("");
}

function home() {
	return process.env.CODEX_HOME ?? join(homedir(), ".codex");
}

function stateFile(sessionId) {
	const directory = join(home(), "runtime", "compact");
	mkdirSync(directory, { recursive: true });
	const safe = [...sessionId]
		.filter((character) => /[\p{Letter}\p{Number}_-]/u.test(character))
		.join("");
	return join(directory, `${safe}.json`);
}

function tail(path) {
	if (!path) {
		return [];
	}

	let file;
	try {
		file = openSync(path, "r");
		const size = fstatSync(file).size;
		const start = Math.max(0, size - TAIL);
		const buffer = Buffer.alloc(size - start);
		let offset = 0;
		while (offset < buffer.length) {
			const bytesRead = readSync(
				file,
				buffer,
				offset,
				buffer.length - offset,
				start + offset,
			);
			if (bytesRead === 0) {
				break;
			}
			offset += bytesRead;
		}

		let data = buffer.subarray(0, offset);
		if (size > TAIL) {
			const newline = data.indexOf(0x0a);
			data = newline === -1 ? Buffer.alloc(0) : data.subarray(newline + 1);
		}
		return new TextDecoder().decode(data).split(/\r?\n/);
	} catch {
		return [];
	} finally {
		if (file !== undefined) {
			try {
				closeSync(file);
			} catch {
				// The bounded transcript read is best effort.
			}
		}
	}
}

function extractText(content) {
	if (typeof content === "string") {
		return content;
	}
	if (!Array.isArray(content)) {
		return "";
	}

	return content
		.filter((item) => isObject(item) && typeof item.text === "string")
		.map((item) => item.text)
		.join("\n");
}

function recent(path) {
	let user;
	let assistant;

	for (const line of tail(path).reverse()) {
		let event;
		try {
			event = JSON.parse(line);
		} catch {
			continue;
		}

		if (!isObject(event) || event.type !== "response_item") {
			continue;
		}
		const payload = event.payload;
		if (!isObject(payload) || payload.type !== "message") {
			continue;
		}

		const text = extractText(payload.content).trim();
		if (!text) {
			continue;
		}
		if (payload.role === "assistant" && assistant === undefined) {
			assistant = limitStart(text, MESSAGE_CAP);
		} else if (payload.role === "user" && user === undefined) {
			user = limitStart(text, MESSAGE_CAP);
		}
		if (user !== undefined && assistant !== undefined) {
			break;
		}
	}

	return [user ?? "", assistant ?? ""];
}

function gitState(cwd) {
	if (!cwd) {
		return "";
	}

	function run(...args) {
		try {
			const result = spawnSync("git", ["-C", cwd, ...args], {
				encoding: "utf8",
				timeout: 3000,
			});
			return result.status === 0 ? result.stdout.trim() : "";
		} catch {
			return "";
		}
	}

	const branch = run("branch", "--show-current");
	const head = run("rev-parse", "--short", "HEAD");
	const status = run("status", "--short", "--untracked-files=normal");
	if (!branch && !head && !status) {
		return "";
	}

	let snapshot = `branch=${branch || "(detached)"} head=${head || "?"}`;
	if (status) {
		snapshot += `\n${limitStart(status, 3500)}`;
	}
	return snapshot;
}

function save(event) {
	const sessionId = String(event.session_id ?? "");
	if (!sessionId) {
		return;
	}

	const [user, assistant] = recent(
		typeof event.transcript_path === "string" ? event.transcript_path : "",
	);
	const cwd = typeof event.cwd === "string" ? event.cwd : ".";
	const data = { user, assistant, git: gitState(cwd) };

	try {
		writeFileSync(stateFile(sessionId), JSON.stringify(data), "utf8");
	} catch {
		// Checkpoint persistence is best effort.
	}
}

function restore(event) {
	if (event.source !== "compact") {
		return;
	}

	const sessionId = String(event.session_id ?? "");
	if (!sessionId) {
		return;
	}

	let data;
	try {
		data = JSON.parse(readFileSync(stateFile(sessionId), "utf8"));
	} catch {
		return;
	}
	if (!isObject(data)) {
		return;
	}

	const parts = [
		"<compact_recovery>",
		"Continue the active task; do not start a new conversation or ask for a new task when the objective is recoverable.",
	];
	if (typeof data.user === "string" && data.user) {
		parts.push("Latest user objective:", data.user);
	}
	if (typeof data.assistant === "string" && data.assistant) {
		parts.push("Last visible task state:", data.assistant);
	}
	if (typeof data.git === "string" && data.git) {
		parts.push("Current captured git state:", data.git);
	}
	parts.push(
		"Verify against the current worktree before editing; preserve existing completed work.",
		"</compact_recovery>",
	);

	process.stdout.write(
		`${JSON.stringify({
			hookSpecificOutput: {
				hookEventName: "SessionStart",
				additionalContext: limitEnd(parts.join("\n"), TOTAL_CAP),
			},
		})}\n`,
	);
}

function main(input) {
	let event;
	try {
		event = JSON.parse(input);
	} catch {
		return;
	}
	if (!isObject(event)) {
		return;
	}

	if (event.hook_event_name === "PreCompact") {
		save(event);
	} else if (event.hook_event_name === "SessionStart") {
		restore(event);
	}
}

main(await Bun.stdin.text());
