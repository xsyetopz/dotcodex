#!/bin/zsh
set -euo pipefail

if ! command -v headroom >/dev/null 2>&1; then
  if ! command -v uv >/dev/null 2>&1; then
    print -u2 -- "headroom is not on PATH and uv is unavailable."
    print -u2 -- "Install headroom-ai[mcp] using an upstream-supported Python environment."
    exit 1
  fi
  uv tool install --python 3.13 "headroom-ai[mcp]"
fi

headroom --version

# Current Headroom exposes --agent; refuse instead of inventing a manual fallback.
if ! headroom mcp install --help 2>&1 | grep -q -- "--agent"; then
  print -u2 -- "This Headroom build does not expose agent-specific MCP registration."
  print -u2 -- "No Codex configuration was changed."
  exit 2
fi

headroom mcp install --agent codex --force
headroom mcp status
print -- "Restart Codex."
