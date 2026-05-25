#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib.sh"

build_site
assert_file_exists "$BUILD_DIR/authors/index.html"

authors=$(grep -h '^author:' "$ROOT_DIR"/library/*.md | sed 's/^author:[[:space:]]*//' | sort -u)

while IFS= read -r author; do
  [[ -z "$author" ]] && continue
  slug=$(echo "$author" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g')
  assert_file_exists "$BUILD_DIR/authors/${slug}/index.html"
done <<< "$authors"

echo "Phase 2 authors pages passed"
