#!/bin/zsh
set -euo pipefail
HERE="${0:A:h}"
"$HERE/setup-codegraph.zsh"
print -- "\n----------------------------------------\n"
"$HERE/setup-headroom.zsh"
