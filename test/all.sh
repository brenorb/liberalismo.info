#!/usr/bin/env bash
set -euo pipefail

scripts=(
  test/smoke.sh
  test/language_standard.sh
  test/repo_hygiene.sh
  test/work_the_law.sh
  test/library_fulltext.sh
  test/library_index.sh
  test/library_schema.sh
  test/authors_pages.sh
  test/taxonomy.sh
  test/faq_coverage.sh
  test/reading_paths.sh
  test/link_integrity.sh
  test/search_index.sh
  test/search_quality.sh
)

for script in "${scripts[@]}"; do
  echo "==> $script"
  "$script"
  echo

done

echo "All tests passed"
