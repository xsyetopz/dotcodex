from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts/validate_codex_harness.py"
SPEC = importlib.util.spec_from_file_location("validate_codex_harness", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class HarnessConfigurationTests(unittest.TestCase):
    def test_merges_nested_profile_configuration(self) -> None:
        base = {"tools": {"update_plan": {"enabled": True}}, "model": "base"}
        profile = {"tools": {"other": {"enabled": False}}, "model": "profile"}

        effective = VALIDATOR.merged(base, profile)

        self.assertEqual(effective["model"], "profile")
        self.assertTrue(effective["tools"]["update_plan"]["enabled"])
        self.assertFalse(effective["tools"]["other"]["enabled"])

    def test_maps_profiles_to_model_specific_prompts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.create_fixture(Path(directory))

            configurations = VALIDATOR.validate_configuration(root)

            by_profile = {
                profile: (config["model"], prompt.name)
                for profile, config, prompt in configurations
            }
            self.assertEqual(by_profile, VALIDATOR.EXPECTED_PROFILE_CONTRACTS)
            self.assertEqual(
                by_profile["security"], ("gpt-daybreak-blue-latest", "sol.md")
            )

    def test_rejects_profile_fallback_to_wrong_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.create_fixture(Path(directory))
            security = root / "security.config.toml"
            security.write_text(
                security.read_text(encoding="utf-8").replace("sol.md", "astra.md"),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "security must use .*sol.md"):
                VALIDATOR.validate_configuration(root)

    def test_astra_contract_requires_proposed_plan_route(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.create_fixture(Path(directory))
            astra = root / "model-instructions/astra.md"
            astra.write_text(
                astra.read_text(encoding="utf-8").replace(
                    "<proposed_plan>\n# Title", "# Title"
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                ValueError, "astra.md is missing contract marker"
            ):
                VALIDATOR.validate_instruction_contract(root)

    def test_rejects_missing_baseline_section(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.create_fixture(Path(directory))
            luna = root / "model-instructions/luna.md"
            luna.write_text(
                luna.read_text(encoding="utf-8").replace("## Goal\ngoal\n\n", ""),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                ValueError, "luna.md is missing baseline section: Goal"
            ):
                VALIDATOR.validate_instruction_contract(root)

    def test_rejects_misordered_baseline_sections(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.create_fixture(Path(directory))
            terra = root / "model-instructions/terra.md"
            terra.write_text(
                terra.read_text(encoding="utf-8").replace(
                    "## Personality\npersonality\n\n## Goal\ngoal",
                    "## Goal\ngoal\n\n## Personality\npersonality",
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                ValueError, "terra.md baseline sections must appear in order"
            ):
                VALIDATOR.validate_instruction_contract(root)

    @staticmethod
    def create_fixture(root: Path) -> Path:
        prompt_directory = root / "model-instructions"
        prompt_directory.mkdir()
        baseline_text = "\n\n".join(
            (
                "# Role\nrole",
                "## Personality\npersonality",
                "## Goal\ngoal",
                "## Success criteria\nsuccess criteria",
                "## Constraints\nconstraints",
                "## Output\noutput",
                "## Stop rules\nstop rules",
            )
        )
        marker_text = "\n".join(VALIDATOR.REQUIRED_CONTRACT_MARKERS)
        for prompt in {
            value[1] for value in VALIDATOR.EXPECTED_PROFILE_CONTRACTS.values()
        }:
            (prompt_directory / prompt).write_text(
                f"{baseline_text}\n\n{marker_text}\nunique: {prompt}\n",
                encoding="utf-8",
            )

        base_model, base_prompt = VALIDATOR.EXPECTED_PROFILE_CONTRACTS[None]
        (root / "config.toml").write_text(
            "\n".join(
                (
                    f'model = "{base_model}"',
                    f'model_instructions_file = "{prompt_directory / base_prompt}"',
                    "include_collaboration_mode_instructions = true",
                    'developer_instructions = "base"',
                    "[tools.update_plan]",
                    "enabled = true",
                )
            ),
            encoding="utf-8",
        )
        for profile, (model, prompt) in VALIDATOR.EXPECTED_PROFILE_CONTRACTS.items():
            if profile is None:
                continue
            (root / f"{profile}.config.toml").write_text(
                "\n".join(
                    (
                        f'model = "{model}"',
                        f'model_instructions_file = "{prompt_directory / prompt}"',
                        f'developer_instructions = "{profile}"',
                    )
                ),
                encoding="utf-8",
            )
        return root


if __name__ == "__main__":
    unittest.main()
