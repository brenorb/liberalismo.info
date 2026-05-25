#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TAXONOMY_FILE="$ROOT_DIR/_data/taxonomies.yml"

if [[ ! -f "$TAXONOMY_FILE" ]]; then
  echo "Missing taxonomy definition: _data/taxonomies.yml"
  exit 1
fi

for key in '^themes:' '^schools:'; do
  if ! grep -q "$key" "$TAXONOMY_FILE"; then
    echo "Taxonomy key missing: $key"
    exit 1
  fi
done

echo "Phase 2 taxonomy passed"
