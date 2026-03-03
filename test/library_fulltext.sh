#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

assert_min_words() {
  local file="$1"
  local min_words="$2"
  local count
  count=$(awk 'BEGIN{in_body=0} /^---$/ {c++; if(c==2){in_body=1; next} else {next}} in_body{print}' "$file" | wc -w | tr -d ' ')
  if [[ "$count" -lt "$min_words" ]]; then
    echo "Expected at least $min_words words in $(basename "$file"), got $count"
    exit 1
  fi
}

assert_min_words "$ROOT_DIR/library/the-law.md" 5000
assert_min_words "$ROOT_DIR/library/on-liberty.md" 8000
assert_min_words "$ROOT_DIR/library/two-treatises.md" 20000
assert_min_words "$ROOT_DIR/library/democracy-in-america.md" 50000
assert_min_words "$ROOT_DIR/library/wealth-of-nations.md" 150000

if ! grep -qi 'copyright' "$ROOT_DIR/library/road-to-serfdom.md"; then
  echo "road-to-serfdom.md must include an explicit copyright status note"
  exit 1
fi

if ! grep -qi 'full text is not reproduced' "$ROOT_DIR/library/road-to-serfdom.md"; then
  echo "road-to-serfdom.md must explain why full text is not hosted"
  exit 1
fi

echo "Library full-text coverage passed"
