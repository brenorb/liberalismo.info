#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib.sh"

library_count=$(find "$ROOT_DIR/library" -maxdepth 1 -name '*.md' ! -name 'index.md' | wc -l | tr -d ' ')
if [[ "$library_count" -lt 500 ]]; then
  echo "Expected at least 500 library works, got $library_count"
  exit 1
fi

if rg -q 'Project Gutenberg eBook|\*\*\* START OF|\*\*\* END OF|Section 1\. General Terms of Use and Redistributing Project Gutenberg' "$ROOT_DIR/library"; then
  echo "Library still contains Project Gutenberg boilerplate"
  exit 1
fi

build_site
python3 - "$BUILD_DIR/search.json" "$library_count" <<'PY'
import json
import sys

path = sys.argv[1]
expected = int(sys.argv[2])
items = json.load(open(path))
if len(items) < expected:
    raise SystemExit(f"Expected at least {expected} search entries, got {len(items)}")
PY

echo "Catalog scale passed"
