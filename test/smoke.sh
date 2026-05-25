#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$ROOT_DIR/.site-test"

rm -rf "$BUILD_DIR"
if ! bundle exec jekyll build --destination "$BUILD_DIR" >/tmp/jekyll-build.log 2>&1; then
  cat /tmp/jekyll-build.log
  exit 1
fi

for page in index.html about/index.html library/index.html library/the-law/index.html authors/index.html themes/index.html schools/index.html docs/VISION/index.html docs/SPEC/index.html docs/ROADMAP/index.html docs/FAQ/index.html docs/READING_PATHS/index.html search/index.html search.json; do
  if [[ ! -f "$BUILD_DIR/$page" ]]; then
    echo "Missing generated page: $page"
    exit 1
  fi
done

grep -q "Liberalismo.info" "$BUILD_DIR/about/index.html"
grep -q "The Law (A Lei)" "$BUILD_DIR/library/index.html"
grep -q "Open archive of liberal texts" "$BUILD_DIR/index.html"
grep -q "Portuguese (pt-BR)" "$BUILD_DIR/index.html"
if grep -q "My website" "$BUILD_DIR/index.html"; then
  echo "Template homepage title still present"
  exit 1
fi

echo "Smoke test passed"
