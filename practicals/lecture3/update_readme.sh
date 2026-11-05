#!/usr/bin/env bash
set -euo pipefail
result=${1:?vowel result required}
actor=${2:?GitHub username required}
report=${README_PATH:-README.md}
printf '\n### Updated by %s on %s [Commit: %s]\n\nVowel counts: `%s`\n' "$actor" "$(date -u '+%Y-%m-%d %H:%M:%S UTC')" "${SOURCE_SHA:-local}" "$result" >> "$report"
