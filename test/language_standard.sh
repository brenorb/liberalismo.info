#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# English-first markers
if ! grep -q '^subtitle: Open archive of liberal texts' "$ROOT_DIR/index.md"; then
  echo "index.md is not English-first"
  exit 1
fi

if ! grep -q '^title: About' "$ROOT_DIR/about.md"; then
  echo "about.md is not English-first"
  exit 1
fi

if ! grep -q '^title: Vision' "$ROOT_DIR/docs/VISION.md"; then
  echo "VISION.md is not English-first"
  exit 1
fi

# Portuguese secondary section markers
for file in index.md about.md docs/FAQ.md docs/READING_PATHS.md; do
  if ! grep -q '## Portuguese (pt-BR)' "$ROOT_DIR/$file"; then
    echo "Missing Portuguese secondary section in $file"
    exit 1
  fi
done

echo "Language standard passed"
