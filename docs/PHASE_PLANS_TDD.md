---
layout: page
title: Phase Plans (TDD)
subtitle: Test-driven execution plan for each roadmap phase
permalink: /docs/PHASE_PLANS_TDD/
---

# Liberalismo.info - Phase Plans with TDD

This document converts the roadmap into executable Red -> Green -> Refactor plans.

## Global TDD rules
- Every PR starts with failing test(s).
- New tests must fail for the intended reason.
- Implement the smallest change to go green.
- Refactor only after green.
- Minimum merge gate: `./test/smoke.sh`.

## Phase 0 - Repository organization
### Objective
Keep the base coherent, buildable, and free of template leftovers.

### Red
- `test/smoke.sh` for build + core pages.
- `test/repo_hygiene.sh` for template artifact detection.

### Green
- Align dependencies with local runtime.
- Replace template homepage with project landing page.
- Remove/archive template demo content.

### Refactor
- Standardize test scripts under `test/`.
- Keep README setup/test instructions current.

## Phase 1 - MVP (The Law)
### Objective
Publish one full work with reliable metadata and navigation.

### Red
- `test/work_the_law.sh` validates minimum metadata + substantial text body.
- `test/library_index.sh` validates library listing and links.

### Green
- Complete `library/the-law.md` metadata + text.
- Keep `/library/` index aligned.

### Refactor
- Reuse front matter checks across content tests.

## Phase 2 - Initial scale
### Objective
Expand the catalog with consistency.

### Red
- `test/library_schema.sh` checks minimum schema across works.
- `test/authors_pages.sh` ensures every referenced author has a page.
- `test/taxonomy.sh` checks taxonomy definitions.

### Green
- Add additional works with complete metadata.
- Add author pages and taxonomy data.

### Refactor
- Use structured data where it reduces duplication.

## Phase 3 - Curation and FAQ
### Objective
Add a useful editorial layer without losing archive discipline.

### Red
- `test/faq_coverage.sh` for required FAQ sections.
- `test/reading_paths.sh` for path sections and minimum items.
- `test/link_integrity.sh` for internal cross-link integrity.

### Green
- Publish FAQ answers.
- Publish reading path pages with references.

### Refactor
- Improve clarity and consistency of editorial language.

## Phase 4 - Search and discoverability
### Objective
Improve findability through searchable structured data.

### Red
- `test/search_index.sh` validates search endpoints and schema.
- `test/search_quality.sh` validates key query coverage.

### Green
- Publish `/search/` UI and `/search.json` index.

### Refactor
- Iterate search relevance and ranking strategy.

## Suggested execution order
1. Phase 0 baseline stability.
2. Phase 1 flagship quality.
3. Phase 2 catalog growth in small batches.
4. Phase 3 curation quality.
5. Phase 4 search quality iteration.

## Portuguese (pt-BR)
Plano operacional em TDD para executar roadmap por fases com gates de teste.
