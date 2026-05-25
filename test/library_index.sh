#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib.sh"

build_site
assert_file_exists "$BUILD_DIR/library/index.html"

while IFS= read -r file; do
  slug="$(basename "$file" .md)"
  [[ "$slug" == "index" ]] && continue
  assert_contains "/library/${slug}/" "$BUILD_DIR/library/index.html"
done < <(find "$ROOT_DIR/library" -maxdepth 1 -name '*.md' | sort)

echo "Phase 1 library index passed"
