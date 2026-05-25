#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK_FILE="$ROOT_DIR/library/the-law.md"

for field in '^title:' '^author:' '^year_first_published:' '^original_language:' '^source_url:' '^tags:'; do
  if ! grep -q "$field" "$WORK_FILE"; then
    echo "Missing required field in the-law.md: $field"
    exit 1
  fi
done

if grep -q 'TODO' "$WORK_FILE"; then
  echo "The Law page still has TODO markers"
  exit 1
fi

word_count=$(awk 'BEGIN{in_body=0} /^---$/ {c++; if(c==2){in_body=1; next} else {next}} in_body{print}' "$WORK_FILE" | wc -w | tr -d ' ')
if [[ "$word_count" -lt 900 ]]; then
  echo "The Law body too short: ${word_count} words (expected >= 900)"
  exit 1
fi

echo "Phase 1 The Law content passed"
