set dotenv-load := false

cache := env("CODEX_SUITE_CACHE_DIR", env("HOME") + "/.cache/codex-suite")
venv := cache + "/validation-venv"
bun_cache := cache + "/bun"

default: validate

provision:
    mkdir -p "{{ cache }}" "{{ bun_cache }}"
    test -x "{{ venv }}/bin/python" || python3 -m venv "{{ venv }}"
    "{{ venv }}/bin/python" -m pip install --disable-pip-version-check -r requirements-validation.txt

skills: provision
    for skill in skills/*; do "{{ venv }}/bin/skills-ref" validate "$skill"; done

metadata: provision
    "{{ venv }}/bin/python" scripts/validate_repository.py

harness:
    python3 scripts/validate_codex_harness.py

markdown:
    BUN_INSTALL_CACHE_DIR="{{ bun_cache }}" bunx --bun markdownlint-cli2@0.23.2 "README.md" "docs/**/*.md" "model-instructions/*.md" "skills/audit-codex-execution/**/*.md" "skills/execute-deterministic-workflow/**/*.md" "skills/operate-codex-goals/**/*.md" "skills/orchestrate-codex-agents/**/*.md"

tests:
    PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v

python-lint:
    ruff check hooks scripts skills tests
    ruff format --check hooks scripts skills tests

python-types: provision
    pyright --pythonpath "{{ venv }}/bin/python"

doctor:
    codex --strict-config doctor --summary

validate: skills metadata harness markdown tests python-lint python-types doctor
    git diff --check
