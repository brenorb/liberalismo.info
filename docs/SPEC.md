---
layout: page
title: Specification
subtitle: MVP scope and base structure
permalink: /docs/SPEC/
---

# Liberalismo.info - Specification (v0)

This document describes the MVP and the initial product structure.

## 1. MVP scope
- Start with one flagship work: **"The Law" - Frederic Bastiat**.
- MVP objective: validate content model, page layout, and editorial workflow.

## 2. Long-term scope (not all implemented now)
- Library with full texts and source-linked entries.
- Metadata catalog when full text is not yet included.
- Taxonomies for authors, works, themes, periods, and schools.
- Later layers: curation, essays, guided reading paths, expanded FAQ.

## 3. UX direction
- Dense but navigable archive style with multiple entry points.

## 4. Content model
### 4.1 Core entities
- **Author**
- **Work**
- **Theme** (tags)
- **School** (e.g., classical liberalism, libertarianism, Austrian school)

### 4.2 Minimum fields for work pages
- `title`
- `author`
- `original_language`
- `year_first_published`
- `source_url`
- `tags`

## 5. Navigation baseline
- Work pages under `/library/`
- Author pages under `/authors/`
- Dedicated pages for FAQ, reading paths, and search

## 6. Non-functional requirements
- Static site architecture
- Markdown-first content
- Git-based review and traceability

## Portuguese (pt-BR)
MVP: validar modelo de conteudo, layout e fluxo editorial com uma obra principal, evoluindo para catalogo maior com taxonomias.
