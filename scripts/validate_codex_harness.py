"""Validate the native-prompt Codex 0.154.0 harness contract."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any, Never

ROOT = Path(__file__).parents[1]
EXPECTED_VERSION = "codex-cli 0.154.0"
SENTINEL = "__CODEX_HARNESS_SENTINEL__"
AGENTS_MARKER = "Use one canonical term for each concept."
DEVELOPER_MARKER = "Treat the current request and higher-priority instructions"
EXPECTED_PROFILE_CONTRACTS = {
    None: ("gpt-6-astra", "low", "medium"),
    "coding": ("gpt-5.6-sol", "medium", "medium"),
    "fast-coding": ("gpt-5.6-luna", "high", "medium"),
    "deep-coding": ("gpt-6-astra", "high", "high"),
    "security": ("gpt-daybreak-blue-latest", "medium", "high"),
}
EXPECTED_AGENTS = {
    "cyber_defender": ("gpt-daybreak-blue-latest", "medium", "read-only"),
    "debugger": ("gpt-5.6-sol", "medium", "workspace-write"),
    "docs_researcher": ("gpt-5.6-luna", "high", "read-only"),
    "implementer": ("gpt-5.6-luna", "xhigh", "workspace-write"),
    "reviewer": ("gpt-5.6-sol", "medium", "read-only"),
    "scout": ("gpt-5.6-luna", "high", "read-only"),
}
EXPECTED_SKILLS = {
    "audit-codex-execution": False,
    "operate-codex-goals": True,
    "orchestrate-codex-agents": False,
}
EXPECTED_FEATURES = {
    "collaboration_modes": ("removed", True),
    "context_management": ("under development", False),
    "default_mode_request_user_input": ("under development", True),
    "goals": ("stable", True),
    "hooks": ("stable", True),
    "multi_agent_v2": ("stable", True),
    "sleep_tool": ("stable", True),
    "unified_exec": ("stable", True),
    "view_image": ("stable", True),
}
FEATURE_LINE = re.compile(
    r"^(\S+)\s+(removed|stable|under development|experimental|deprecated)\s+(true|false)$"
)


def fail(message: str) -> Never:
    raise ValueError(message)


def run_codex(*arguments: str) -> str:
    result = subprocess.run(
        ["codex", *arguments],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        env={**os.environ, "CODEX_HOME": str(ROOT)},
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        fail(f"codex {' '.join(arguments)} failed: {detail}")
    return result.stdout


def load_toml(path: Path) -> dict[str, Any]:
    with path.open("rb") as file:
        return tomllib.load(file)


def merged(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    result = base.copy()
    for key, value in override.items():
        current = result.get(key)
        if isinstance(current, dict) and isinstance(value, dict):
            result[key] = merged(current, value)
        else:
            result[key] = value
    return result


def input_texts(value: object) -> list[str]:
    if isinstance(value, list):
        return [text for item in value for text in input_texts(item)]
    if isinstance(value, dict):
        texts = []
        if value.get("type") == "input_text" and isinstance(value.get("text"), str):
            texts.append(value["text"])
        return texts + [
            text
            for key, item in value.items()
            if key not in {"type", "text"}
            for text in input_texts(item)
        ]
    return []


def validate_service_policy(config: dict[str, Any], label: str) -> None:
    if config.get("features", {}).get("fast_mode") is not False:
        fail(f"{label} must disable features.fast_mode")
    if config.get("service_tier") != "default":
        fail(f"{label} must use standard service_tier=default on Codex 0.154.0")


def validate_configuration(
    root: Path = ROOT,
) -> list[tuple[str | None, dict[str, Any]]]:
    base = load_toml(root / "config.toml")
    if "model_instructions_file" in base:
        fail("config.toml must use the native Codex base prompt")
    if base.get("tool_output_token_limit") != 4000:
        fail("config.toml must set tool_output_token_limit to 4000")
    if base.get("include_collaboration_mode_instructions") is not True:
        fail("config.toml must enable collaboration-mode instructions")
    if base.get("tools", {}).get("update_plan", {}).get("enabled") is not True:
        fail("config.toml must enable tools.update_plan")

    features = base.get("features", {})
    for name in ("fast_mode", "goals", "hooks", "unified_exec", "view_image"):
        expected = name != "fast_mode"
        if features.get(name) is not expected:
            fail(f"config.toml must set features.{name}={str(expected).lower()}")
    if "context_management" in features:
        fail("config.toml must not enable experimental context management")

    multi_agent = features.get("multi_agent_v2", {})
    if multi_agent.get("max_concurrent_threads_per_session") != 3:
        fail("multi-agent ceiling must be root plus two children")

    profile_paths = {
        path.name.removesuffix(".config.toml"): path
        for path in root.glob("*.config.toml")
    }
    expected_profiles = set(EXPECTED_PROFILE_CONTRACTS) - {None}
    if set(profile_paths) != expected_profiles:
        fail(
            "profile files do not match the expected set: "
            f"expected {sorted(expected_profiles)}, found {sorted(profile_paths)}"
        )

    configurations = []
    for name, expected in EXPECTED_PROFILE_CONTRACTS.items():
        if name is None:
            profile = {}
        else:
            profile_path = profile_paths[name]
            profile = load_toml(profile_path)
            if "model_instructions_file" in profile:
                fail(f"{profile_path.name} must use the native Codex base prompt")
            if "developer_instructions" in profile:
                fail(f"{profile_path.name} duplicates the developer policy")
        effective = base if name is None else merged(base, profile)
        validate_service_policy(effective, name or "base")
        actual = (
            effective.get("model"),
            effective.get("model_reasoning_effort"),
            effective.get("plan_mode_reasoning_effort"),
        )
        if actual != expected:
            fail(f"{name or 'base'} routing expected {expected}, found {actual}")
        configurations.append((name, effective))

    validate_agents(base, root)
    validate_skills(root)
    return configurations


def validate_agents(base: dict[str, Any], root: Path) -> None:
    agents = {
        name: value
        for name, value in base.get("agents", {}).items()
        if isinstance(value, dict) and "config_file" in value
    }
    if set(agents) != set(EXPECTED_AGENTS):
        fail(
            f"configured agents expected {sorted(EXPECTED_AGENTS)}, found {sorted(agents)}"
        )
    files = {path.name for path in (root / "agents").glob("*.toml")}
    expected_files = {Path(value["config_file"]).name for value in agents.values()}
    if files != expected_files:
        fail(f"agent files expected {sorted(expected_files)}, found {sorted(files)}")
    for name, expected in EXPECTED_AGENTS.items():
        role = load_toml(root / agents[name]["config_file"])
        if "model_instructions_file" in role:
            fail(f"agent {name} must use its model's native prompt")
        actual = (
            role.get("model"),
            role.get("model_reasoning_effort"),
            role.get("sandbox_mode"),
        )
        if actual != expected:
            fail(f"agent {name} routing expected {expected}, found {actual}")
        validate_service_policy(merged(base, role), f"agent {name}")


def validate_skills(root: Path) -> None:
    skills = {
        path.parent.name: path.parent for path in (root / "skills").glob("*/SKILL.md")
    }
    if set(skills) != set(EXPECTED_SKILLS):
        fail(f"skills expected {sorted(EXPECTED_SKILLS)}, found {sorted(skills)}")
    for name, implicit in EXPECTED_SKILLS.items():
        metadata = (skills[name] / "agents" / "openai.yaml").read_text(encoding="utf-8")
        marker = f"allow_implicit_invocation: {str(implicit).lower()}"
        if marker not in metadata:
            fail(f"skill {name} must set {marker}")


def validate_prompt(profile: str | None, config: dict[str, Any]) -> None:
    arguments = [] if profile is None else ["--profile", profile]
    raw = run_codex(*arguments, "debug", "prompt-input", SENTINEL)
    try:
        prompt = json.loads(raw)
    except json.JSONDecodeError as exception:
        fail(f"{profile or 'base'} prompt probe returned invalid JSON: {exception}")
    texts = input_texts(prompt)
    joined = "\n".join(texts)
    label = profile or "base"

    if SENTINEL not in texts:
        fail(f"{label} prompt probe omitted the sentinel user prompt")
    if joined.count(DEVELOPER_MARKER) != 1:
        fail(f"{label} prompt probe must contain one developer policy")
    agents_payloads = [
        text for text in texts if text.startswith("# AGENTS.md instructions")
    ]
    if len(agents_payloads) != 1 or AGENTS_MARKER not in agents_payloads[0]:
        fail(f"{label} prompt probe must contain one AGENTS.md payload")
    skill_catalogs = [
        text for text in texts if text.startswith("<skills_instructions>")
    ]
    if len(skill_catalogs) != 1:
        fail(f"{label} prompt probe expected one skill catalog")
    catalog = skill_catalogs[0]
    if "- operate-codex-goals:" not in catalog:
        fail(f"{label} prompt probe omitted operate-codex-goals")
    for skill in ("audit-codex-execution", "orchestrate-codex-agents"):
        if f"- {skill}:" in catalog:
            fail(f"{label} prompt probe exposed explicit-only skill {skill}")
    if "execute-deterministic-workflow" in joined:
        fail(f"{label} prompt probe contains removed workflow instructions")
    instructions = config.get("developer_instructions")
    if not isinstance(instructions, str) or instructions.strip() not in joined:
        fail(f"{label} prompt probe omitted the shared developer policy")


def validate_features() -> None:
    features = {}
    for line in run_codex("features", "list").splitlines():
        match = FEATURE_LINE.fullmatch(line.strip())
        if match:
            name, stage, enabled = match.groups()
            features[name] = (stage, enabled == "true")
    for name, expected in EXPECTED_FEATURES.items():
        if features.get(name) != expected:
            fail(f"feature {name} expected {expected}, found {features.get(name)}")


def main() -> int:
    try:
        if run_codex("--version").strip() != EXPECTED_VERSION:
            fail(f"codex must be exactly {EXPECTED_VERSION}")
        configurations = validate_configuration()
        validate_features()
        for profile, config in configurations:
            validate_prompt(profile, config)
    except (
        OSError,
        KeyError,
        TypeError,
        ValueError,
        tomllib.TOMLDecodeError,
    ) as exception:
        print(exception, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
