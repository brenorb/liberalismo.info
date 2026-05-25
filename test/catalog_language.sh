#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 - "$ROOT_DIR/_data/catalog.json" <<'PY'
import json
import sys

catalog = json.load(open(sys.argv[1]))
works = catalog["works"]
if len(works) < 500:
    raise SystemExit(f"Expected at least 500 catalog works, got {len(works)}")

non_english = [work["slug"] for work in works if work.get("edition_language") != "en"]
if non_english:
    preview = ", ".join(non_english[:10])
    raise SystemExit(f"Expected English editions only; found non-English works: {preview}")
PY

echo "Catalog language passed"
