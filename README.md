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
Rebuild the structured catalog, author pages, and imported library pages from the curated classical liberal manifest:

```bash
uv run --project tools/book_import \
  book-import sync-classical-catalog \
  --repo-root "$(pwd)"
```
