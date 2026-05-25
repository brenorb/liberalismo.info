#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DESIGN_FILE="$ROOT_DIR/DESIGN.md"

if [[ ! -f "$DESIGN_FILE" ]]; then
  echo "Missing design system file: DESIGN.md"
  exit 1
fi

for required in '^---$' '^name:' '^colors:' '^typography:' '^spacing:' '^components:'; do
  if ! grep -q "$required" "$DESIGN_FILE"; then
    echo "Missing DESIGN.md token block entry: $required"
    exit 1
  fi
done

for section in '^## Overview' '^## Colors' '^## Typography' '^## Components' '^## Page Patterns'; do
  if ! grep -q "$section" "$DESIGN_FILE"; then
    echo "Missing DESIGN.md section: $section"
    exit 1
  fi
done

echo "Design system documentation passed"
