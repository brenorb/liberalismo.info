# book-import

Import public-domain books into `liberalismo.info` markdown pages.

## Setup

```bash
uv sync --project tools/book_import --extra ocr
```

## Ingest one book

```bash
uv run --project tools/book_import book-import ingest \
  --source "https://cdn.mises.org/thelaw.pdf" \
  --title "The Law" \
  --author "Frederic Bastiat" \
  --year 1850 \
  --original-language fr \
  --tags "liberalism,law,state" \
  --repo-root /Users/breno/Documents/code/SITES/liberalismo.info \
  --force-ocr
```

This writes `/Users/breno/Documents/code/SITES/liberalismo.info/library/the-law.md`.

## Evaluate OCR with public-domain books

```bash
uv run --project tools/book_import --extra ocr \
  python tools/book_import/scripts/evaluate_public_domain.py
```

Outputs:
- `tools/book_import/out/imported/*.md`
- `tools/book_import/out/ocr_report.md`
- `tools/book_import/out/ocr_report.json`
