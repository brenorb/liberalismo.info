#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FILE="$ROOT_DIR/docs/READING_PATHS.md"

if [[ ! -f "$FILE" ]]; then
  echo "Missing reading paths file: docs/READING_PATHS.md"
  exit 1
fi

for section in '## Beginner path' '## Intermediate path'; do
  if ! grep -q "$section" "$FILE"; then
    echo "Missing section: $section"
    exit 1
  fi
done

if ! grep -q '## Portuguese (pt-BR)' "$FILE"; then
  echo "Reading paths missing Portuguese secondary section"
  exit 1
fi

if [[ "$(grep -c '^-' "$FILE")" -lt 6 ]]; then
  echo "Reading paths must have at least 6 list items"
  exit 1
fi

echo "Phase 3 reading paths passed"
