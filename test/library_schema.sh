#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

for file in "$ROOT_DIR"/library/*.md; do
  [[ "$(basename "$file")" == "index.md" ]] && continue
  for field in '^title:' '^author:' '^year_first_published:' '^original_language:' '^source_url:' '^tags:'; do
    if ! grep -q "$field" "$file"; then
      echo "Missing field $field in $(basename "$file")"
      exit 1
    fi
  done

done

echo "Phase 2 library schema passed"
