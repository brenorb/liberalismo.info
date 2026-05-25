#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ -f "$ROOT_DIR/aboutme.md" ]]; then
  echo "Template file still present: aboutme.md"
  exit 1
fi

if find "$ROOT_DIR/_posts" -maxdepth 1 -type f | grep -q .; then
  echo "Template/sample posts still present in _posts/"
  exit 1
fi

if [[ -f "$ROOT_DIR/index.html" ]]; then
  echo "Template homepage file still present: index.html"
  exit 1
fi

if grep -R --line-number -E "Inigo Montoya|My website|deanattali" "$ROOT_DIR" \
  --exclude-dir=.git --exclude-dir=.site-test --exclude-dir=.specstory --exclude-dir=test \
  --exclude=css/bootstrap.css.map --exclude=CHANGELOG.md; then
  echo "Template strings found in repository"
  exit 1
fi

echo "Phase 0 hygiene passed"
