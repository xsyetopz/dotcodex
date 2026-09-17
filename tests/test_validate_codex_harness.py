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
    def test_rejects_fast_or_nonstandard_service_overrides(self) -> None:
        base = {"features": {"fast_mode": False}, "service_tier": "default"}
        VALIDATOR.validate_service_policy(base, "base")
        for override in (
            {"features": {"fast_mode": True}},
            {"service_tier": "priority"},
            {"service_tier": "fast"},
            {"service_tier": "flex"},
            {"service_tier": "standard"},
        ):
            with self.subTest(override=override), self.assertRaises(ValueError):
                VALIDATOR.validate_service_policy(
                    VALIDATOR.merged(base, override), "profile"
                )

    def test_merges_nested_profile_configuration(self) -> None:
        base = {"tools": {"update_plan": {"enabled": True}}, "model": "base"}
        profile = {"tools": {"other": {"enabled": False}}, "model": "profile"}

        effective = VALIDATOR.merged(base, profile)

        self.assertEqual(effective["model"], "profile")
        self.assertTrue(effective["tools"]["update_plan"]["enabled"])
        self.assertFalse(effective["tools"]["other"]["enabled"])

    def test_live_configuration_uses_native_prompt_and_expected_routing(self) -> None:
        configurations = VALIDATOR.validate_configuration(ROOT)

        actual = {
            profile: (
                config["model"],
                config["model_reasoning_effort"],
                config["plan_mode_reasoning_effort"],
            )
            for profile, config in configurations
        }

        self.assertEqual(actual, VALIDATOR.EXPECTED_PROFILE_CONTRACTS)

    def test_rejects_custom_prompt_override(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_fixture(Path(directory))
            config = root / "config.toml"
            config.write_text(
                config.read_text(encoding="utf-8").replace(
                    'model = "gpt-6-astra"',
                    'model_instructions_file = "replacement.md"\nmodel = "gpt-6-astra"',
                    1,
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "native Codex base prompt"):
                VALIDATOR.validate_configuration(root)

    def test_rejects_duplicate_profile_developer_policy(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_fixture(Path(directory))
            profile = root / "coding.config.toml"
            profile.write_text(
                profile.read_text(encoding="utf-8").replace(
                    'model = "gpt-5.6-sol"',
                    'developer_instructions = "duplicate"\nmodel = "gpt-5.6-sol"',
                    1,
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "duplicates the developer policy"):
                VALIDATOR.validate_configuration(root)

    @staticmethod
    def copy_fixture(root: Path) -> Path:
        for name in (
            "config.toml",
            "coding.config.toml",
            "fast-coding.config.toml",
            "deep-coding.config.toml",
            "security.config.toml",
        ):
            (root / name).write_bytes((ROOT / name).read_bytes())
        for directory in ("agents", "skills"):
            source = ROOT / directory
            for path in source.rglob("*"):
                if path.is_file():
                    target = root / path.relative_to(ROOT)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(path.read_bytes())
        return root


if __name__ == "__main__":
    unittest.main()
