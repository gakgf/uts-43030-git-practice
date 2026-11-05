#!/usr/bin/env bash
set -euo pipefail
result=$(python /app/frequency.py "${FILE:-data.txt}")
printf '%s\n' "$result"
bash /app/update_readme.sh "$result" "${GITHUB_USER:-local}"
echo 'Vowel analysis completed successfully.'
