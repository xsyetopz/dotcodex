"""Validate custom skill metadata and internal Markdown links."""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

import yaml

LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)")
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED_POLICY = {
    "audit-codex-execution": False,
    "operate-codex-goals": True,
    "orchestrate-codex-agents": False,
}


def error(message: str) -> None:
    print(message, file=sys.stderr)


def load_yaml(path: Path) -> object:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main() -> int:
    errors = 0
    skill_files = sorted(Path("skills").glob("*/SKILL.md"))
    if {path.parent.name for path in skill_files} != set(EXPECTED_POLICY):
        error("skills: expected exactly the three custom skill packages")
        errors += 1

    for skill_file in skill_files:
        skill = skill_file.parent
        text = skill_file.read_text(encoding="utf-8")
        try:
            _, frontmatter, _ = text.split("---", 2)
            metadata = yaml.safe_load(frontmatter)
            if not isinstance(metadata, dict):
                raise TypeError("frontmatter must be a mapping")
        except (TypeError, ValueError, yaml.YAMLError) as exception:
            error(f"{skill_file}: invalid frontmatter: {exception}")
            errors += 1
            continue

        name = skill.name
        if metadata.get("name") != name or not NAME.fullmatch(name):
            error(f"{skill_file}: name must match its valid directory name")
            errors += 1

        openai_file = skill / "agents/openai.yaml"
        try:
            openai = load_yaml(openai_file)
            if not isinstance(openai, dict):
                raise TypeError("metadata must be a mapping")
            interface = openai["interface"]
            policy = openai["policy"]
            if not isinstance(interface, dict) or not isinstance(policy, dict):
                raise TypeError("interface and policy must be mappings")
            fields = ("display_name", "short_description", "default_prompt")
            if not all(isinstance(interface.get(field), str) for field in fields):
                raise TypeError("interface fields must be strings")
            if f"${name}" not in interface["default_prompt"]:
                raise ValueError("default_prompt must name the skill")
            if policy.get("allow_implicit_invocation") is not EXPECTED_POLICY[name]:
                raise ValueError("invocation policy does not match the skill boundary")
        except (KeyError, OSError, TypeError, ValueError, yaml.YAMLError) as exception:
            error(f"{openai_file}: invalid OpenAI metadata: {exception}")
            errors += 1

        for markdown in skill.rglob("*.md"):
            for target in LINK.findall(markdown.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("mailto:"):
                    continue
                if not (markdown.parent / target).resolve().exists():
                    error(f"{markdown}: missing link target {target}")
                    errors += 1

    try:
        config = tomllib.loads(Path("config.toml").read_text(encoding="utf-8"))
        agents = config["agents"]
        if not isinstance(agents, dict):
            raise TypeError("agents must be a table")
        for name, entry in agents.items():
            if not isinstance(entry, dict) or "config_file" not in entry:
                continue
            agent_file = Path(entry["config_file"])
            agent = tomllib.loads(agent_file.read_text(encoding="utf-8"))
            if agent.get("name") != name:
                error(f"{agent_file}: name does not match config.toml key {name}")
                errors += 1
            if agent.get("description") != entry.get("description"):
                error(f"{agent_file}: description is not synchronized with config.toml")
                errors += 1
    except (KeyError, OSError, TypeError, tomllib.TOMLDecodeError) as exception:
        error(f"config.toml: invalid agent registry: {exception}")
        errors += 1

    return int(errors > 0)


if __name__ == "__main__":
    raise SystemExit(main())
