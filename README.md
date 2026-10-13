# Liberalismo.info

Open-source collaborative educational site about **liberalism** and related traditions.

## What It Is
`liberalismo.info` is a navigable library of liberal ideas: to **catalog**, **contextualize**, and **share texts and references**.

- Vision: `docs/VISION.md`
- Specification: `docs/SPEC.md`
- Roadmap: `docs/ROADMAP.md`
- Phase plans (TDD): `docs/PHASE_PLANS_TDD.md`

## Language Standard
English is the default publishing language.
Portuguese (`pt-BR`) is provided as secondary content on core pages.

## Current Status
Archive shell live with a generated catalog, author pages, reading paths, and search.

- Library index: `library/index.md`
- Catalog data: `_data/catalog.json`
- Catalog snapshot source: `tools/book_import/src/book_import/classical_catalog_data.json`
- Batch sync command: `uv run --project tools/book_import book-import sync-classical-catalog --repo-root $(pwd)`

## Local Development
This repo uses Jekyll (Beautiful Jekyll theme).

### Setup
```bash
bundle install
```

### Build
```bash
bundle exec jekyll build
```

### Smoke test
```bash
./test/smoke.sh
```

### Full phase suite
```bash
./test/all.sh
```

## Catalog Sync
Rebuild the structured catalog, author pages, and library pages from the checked-in English-language archive snapshot:

```bash
uv run --project tools/book_import \
  book-import sync-classical-catalog \
  --repo-root "$(pwd)"
```

The current snapshot publishes:
- 500 works in English
- 5 hosted full-text works for core canonical texts
- 1 guide page for `The Road to Serfdom`

## Edit a page

Each HTML page links to its source file in the GitHub editor. The button uses
`page.path`, so custom public permalinks still point to the correct Markdown
file. GitHub handles sign-in and the proposed change/pull request workflow.

The destination is configured with `repository_url` and `repository_branch` in
`_config.yml`; the current default branch is `main`. Forks should update both
values. Set `edit_page: false` in a page’s front matter to hide its button.

Verify source destinations and path escaping with `./test/edit_page.sh`.
