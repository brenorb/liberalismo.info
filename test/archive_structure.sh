#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib.sh"

build_site

assert_file_exists "$BUILD_DIR/themes/index.html"
assert_file_exists "$BUILD_DIR/schools/index.html"
assert_contains 'Browse the archive' "$BUILD_DIR/index.html"
assert_contains '/authors/' "$BUILD_DIR/index.html"
assert_contains '/themes/' "$BUILD_DIR/index.html"
assert_contains '/schools/' "$BUILD_DIR/index.html"
assert_contains 'Browse by theme' "$BUILD_DIR/library/index.html"
assert_contains 'classical-liberalism' "$BUILD_DIR/schools/index.html"
assert_contains 'limited-government' "$BUILD_DIR/themes/index.html"

echo "Archive structure passed"
