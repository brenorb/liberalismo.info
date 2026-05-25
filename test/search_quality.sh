#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib.sh"

build_site
if ! grep -qi 'bastiat' "$BUILD_DIR/search.json"; then
  echo "Expected Bastiat entry in search index"
  exit 1
fi
assert_contains '/library/the-law/' "$(echo "$BUILD_DIR/search.json")"
assert_contains '/library/on-liberty/' "$(echo "$BUILD_DIR/search.json")"

echo "Phase 4 search quality passed"
