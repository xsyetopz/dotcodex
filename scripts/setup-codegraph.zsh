#!/bin/zsh
set -euo pipefail

if ! command -v codegraph >/dev/null 2>&1; then
  print -u2 -- "codegraph is not on PATH."
  print -u2 -- "This setup expects colbymchenry/codegraph 1.6.0."
  exit 1
fi

version="$(codegraph --version 2>/dev/null || true)"
print -- "CodeGraph: ${version:-unknown}"

if [[ "$version" != *"1.6.0"* ]]; then
  print -u2 -- "Expected CodeGraph 1.6.0; refusing to assume another CLI surface."
  exit 2
fi

codegraph install --target=codex --location=global --yes
codegraph install --print-config codex

print -- "Restart Codex."
print -- "Run 'codegraph init' separately from each source repository root."
