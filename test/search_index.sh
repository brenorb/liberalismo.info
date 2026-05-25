#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib.sh"

build_site
assert_file_exists "$BUILD_DIR/search/index.html"
assert_file_exists "$BUILD_DIR/search.json"
assert_contains '"title"' "$BUILD_DIR/search.json"
assert_contains '"url"' "$BUILD_DIR/search.json"
assert_contains '"author"' "$BUILD_DIR/search.json"

echo "Phase 4 search index passed"
