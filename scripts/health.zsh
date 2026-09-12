#!/bin/zsh
set -u

print -- "Codex:"
codex --version 2>/dev/null || print -- "  unavailable"

print -- "\nCodeGraph:"
if command -v codegraph >/dev/null 2>&1; then
  codegraph --version 2>/dev/null || true
  codegraph install --print-config codex 2>/dev/null || true
else
  print -- "  unavailable"
fi

print -- "\nHeadroom:"
if command -v headroom >/dev/null 2>&1; then
  headroom --version 2>/dev/null || true
  headroom mcp status 2>/dev/null || true
else
  print -- "  unavailable"
fi

print -- "\nConfigured agents:"
find "${CODEX_HOME:-$HOME/.codex}/agents" -maxdepth 1 -type f -name '*.toml' -print 2>/dev/null | sort
