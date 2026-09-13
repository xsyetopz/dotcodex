"""Validate the Codex 0.154.0 harness contract and prompt composition."""

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
PROMPT_DIRECTORY_NAME = "model-instructions"
EXPECTED_VERSION = "codex-cli 0.154.0"
SENTINEL = "__CODEX_HARNESS_SENTINEL__"
AGENTS_MARKER = "Keep code simple and responsibilities narrow."
IMPLICIT_SKILLS = ("execute-deterministic-workflow", "operate-codex-goals")
EXPLICIT_SKILLS = ("audit-codex-execution", "orchestrate-codex-agents")
EXPECTED_PROFILE_CONTRACTS = {
    None: ("gpt-5.6-sol", "sol.md"),
    "coding": ("gpt-5.6-terra", "terra.md"),
    "fast-coding": ("gpt-5.6-luna", "luna.md"),
    "deep-coding": ("gpt-6-astra", "astra.md"),
    "security": ("gpt-daybreak-blue-latest", "sol.md"),
}
BASELINE_SECTIONS = (
    ("Role", re.compile(r"^# Role$", re.MULTILINE)),
    ("Personality", re.compile(r"^## Personality$", re.MULTILINE)),
    ("Goal", re.compile(r"^## Goal$", re.MULTILINE)),
    ("Success criteria", re.compile(r"^## Success criteria$", re.MULTILINE)),
    ("Constraints", re.compile(r"^## Constraints$", re.MULTILINE)),
    ("Output", re.compile(r"^## Output$", re.MULTILINE)),
    ("Stop rules", re.compile(r"^## Stop rules$", re.MULTILINE)),
)
REQUIRED_CONTRACT_MARKERS = (
    "active collaboration-mode block",
    "`update_plan` is an execution checklist, not a collaboration mode",
    "<proposed_plan>\n# Title",
    "A Plan request is not satisfied by saying that",
    "`request_user_input` only when",
    "Use `create_goal` only",
    "Use a named role",
    "`wait_agent` once",
    "`functions.wait`",
    "`cell_id`",
    "`session_id`",
    "Use the free-form `apply_patch` tool",
    "Prefer MCP resources and resource templates",
    "approval or permission",
    "Use `view_image` for local images",
)
EXPECTED_FEATURES = {
    "collaboration_modes": ("removed", True),
    "default_mode_request_user_input": ("under development", True),
    "goals": ("stable", True),
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


def resolve_prompt_path(config: dict[str, Any], root: Path) -> Path:
    raw_path = config.get("model_instructions_file")
    if not isinstance(raw_path, str) or not raw_path:
        fail("model_instructions_file must be a nonempty path")
    path = Path(raw_path).expanduser()
    if not path.is_absolute():
        path = root / path
    if not path.is_file():
        fail(f"model instruction file does not exist: {path}")
    resolved = path.resolve()
    try:
        resolved.relative_to((root / PROMPT_DIRECTORY_NAME).resolve())
    except ValueError:
        fail(f"model instruction file is outside {PROMPT_DIRECTORY_NAME}: {path}")
    return resolved


def validate_configuration(
    root: Path = ROOT,
) -> list[tuple[str | None, dict[str, Any], Path]]:
    base = load_toml(root / "config.toml")
    if base.get("include_collaboration_mode_instructions") is not True:
        fail("config.toml must enable collaboration-mode instructions")
    if base.get("tools", {}).get("update_plan", {}).get("enabled") is not True:
        fail("config.toml must enable tools.update_plan")

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

    configurations: list[tuple[str | None, dict[str, Any], Path]] = []
    for name in EXPECTED_PROFILE_CONTRACTS:
        path = root / "config.toml" if name is None else profile_paths[name]
        profile = load_toml(path)
        if profile.get("include_collaboration_mode_instructions") is False:
            fail(f"{path.name} disables collaboration-mode instructions")
        effective = base if name is None else merged(base, profile)
        if effective.get("include_collaboration_mode_instructions") is not True:
            fail(f"{path.name} does not enable collaboration-mode instructions")
        if effective.get("tools", {}).get("update_plan", {}).get("enabled") is not True:
            fail(f"{path.name} does not enable tools.update_plan")
        expected_model, expected_prompt = EXPECTED_PROFILE_CONTRACTS[name]
        if effective.get("model") != expected_model:
            fail(
                f"{name or 'base'} must use model {expected_model}, "
                f"found {effective.get('model')}"
            )
        prompt_path = resolve_prompt_path(effective, root)
        expected_path = (root / PROMPT_DIRECTORY_NAME / expected_prompt).resolve()
        if prompt_path != expected_path:
            fail(f"{name or 'base'} must use {expected_path}, found {prompt_path}")
        configurations.append((name, effective, prompt_path))
    return configurations


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
    instructions = config.get("developer_instructions")
    if not isinstance(instructions, str) or instructions.strip() not in joined:
        fail(f"{label} prompt probe omitted its developer instructions")
    if AGENTS_MARKER not in joined:
        fail(f"{label} prompt probe omitted AGENTS.md")
    skill_catalogs = [
        text for text in texts if text.startswith("<skills_instructions>")
    ]
    if len(skill_catalogs) != 1:
        fail(f"{label} prompt probe expected one skill catalog")
    catalog = skill_catalogs[0]
    for skill in IMPLICIT_SKILLS:
        if f"- {skill}:" not in catalog:
            fail(f"{label} prompt probe omitted implicit skill {skill}")
    for skill in EXPLICIT_SKILLS:
        if f"- {skill}:" in catalog:
            fail(f"{label} prompt probe exposed explicit-only skill {skill}")


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


def validate_instruction_contract(root: Path = ROOT) -> None:
    prompt_directory = root / PROMPT_DIRECTORY_NAME
    expected_files = {contract[1] for contract in EXPECTED_PROFILE_CONTRACTS.values()}
    prompt_files = {path.name: path for path in prompt_directory.glob("*.md")}
    if set(prompt_files) != expected_files:
        fail(
            "model prompt files do not match the expected set: "
            f"expected {sorted(expected_files)}, found {sorted(prompt_files)}"
        )

    contents = {
        name: path.read_text(encoding="utf-8") for name, path in prompt_files.items()
    }
    if len(set(contents.values())) != len(contents):
        fail("model prompt files must not duplicate one another")
    for name, instructions in contents.items():
        section_positions = []
        for section, pattern in BASELINE_SECTIONS:
            match = pattern.search(instructions)
            if match is None:
                fail(f"{name} is missing baseline section: {section}")
            section_positions.append(match.start())
        if section_positions != sorted(section_positions):
            order = " -> ".join(section for section, _ in BASELINE_SECTIONS)
            fail(f"{name} baseline sections must appear in order: {order}")
        for marker in REQUIRED_CONTRACT_MARKERS:
            if marker not in instructions:
                fail(f"{name} is missing contract marker: {marker}")


def main() -> int:
    try:
        if run_codex("--version").strip() != EXPECTED_VERSION:
            fail(f"codex must be exactly {EXPECTED_VERSION}")
        configurations = validate_configuration()
        validate_instruction_contract()
        validate_features()
        for profile, config, _ in configurations:
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
