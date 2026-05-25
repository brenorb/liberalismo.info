#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib.sh"

build_site

assert_contains '/docs/READING_PATHS/' "$BUILD_DIR/docs/FAQ/index.html"
assert_file_exists "$BUILD_DIR/docs/READING_PATHS/index.html"
assert_file_exists "$BUILD_DIR/library/index.html"
assert_file_exists "$BUILD_DIR/authors/index.html"

echo "Phase 3 link integrity passed"
