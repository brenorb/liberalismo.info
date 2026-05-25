#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$ROOT_DIR/.site-test"
LOG_FILE="/tmp/jekyll-build.log"

build_site() {
  rm -rf "$BUILD_DIR"
  if ! bundle exec jekyll build --destination "$BUILD_DIR" >"$LOG_FILE" 2>&1; then
    cat "$LOG_FILE"
    exit 1
  fi
}

assert_file_exists() {
  local path="$1"
  if [[ ! -f "$path" ]]; then
    echo "Missing file: $path"
    exit 1
  fi
}

assert_contains() {
  local pattern="$1"
  local path="$2"
  if ! grep -q "$pattern" "$path"; then
    echo "Pattern '$pattern' not found in $path"
    exit 1
  fi
}
