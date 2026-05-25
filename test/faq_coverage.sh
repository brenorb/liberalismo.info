#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FAQ_FILE="$ROOT_DIR/docs/FAQ.md"

for question in \
  '## What is liberalism?' \
  '## What is the difference between classical liberalism, libertarianism, and the Austrian school?' \
  '## Which texts should I read first?' \
  '## Does the site have a political position?' \
  '## How do you choose translations?' \
  '## Do all entries include full text?'; do
  if ! grep -q "$question" "$FAQ_FILE"; then
    echo "FAQ missing section: $question"
    exit 1
  fi
done

if ! grep -q '## Portuguese (pt-BR)' "$FAQ_FILE"; then
  echo "FAQ missing Portuguese secondary section"
  exit 1
fi

if grep -q 'rascunho' "$FAQ_FILE"; then
  echo "FAQ still marked as draft"
  exit 1
fi

echo "Phase 3 FAQ coverage passed"
