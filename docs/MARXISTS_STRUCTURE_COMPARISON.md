---
layout: page
title: Marxists.org Structure Comparison
subtitle: Gap analysis for library organization
permalink: /docs/MARXISTS_STRUCTURE_COMPARISON/
---

# Marxists.org Structure Comparison

## Observed pattern on Marxists.org
- Archive-first taxonomy under `/archive/<author>/...`.
- Author landing pages list major works and topic links.
- Work pages are often chaptered with internal tables of contents.
- Works frequently expose multiple source formats (`html`, `pdf`, `epub` or mirrors).
- Bibliographic context (date, edition, translators/editors) appears near the top of work pages.

## Current liberalismo.info pattern
- Works are in single markdown files under `library/*.md`.
- Author landing pages exist under `authors/*.md`.
- Library index is a flat list with search integration.
- Required metadata is already enforced by tests (`title`, `author`, `year_first_published`, `original_language`, `source_url`, `tags`).

## Does current structure make sense?
Yes for MVP and editorial control. It is structurally close in spirit (author + work archive with source citations), but less granular than Marxists.org.

## Main gaps vs Marxists.org
- No chapter-level navigation generated automatically.
- No explicit `format`/`edition` surfaced in index-level navigation.
- No per-author sub-archive pathing model in URLs.

## Practical next step
Use an import pipeline that:
1. Converts source books (`pdf/epub/txt/html`) into `library/<slug>.md` with required metadata.
2. Detects chapter headings and emits in-page contents.
3. Preserves source format and extraction strategy in metadata and editorial note.

This keeps the current repo shape while moving UX closer to Marxists-style archive browsing.
