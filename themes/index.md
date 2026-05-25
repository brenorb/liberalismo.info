---
layout: page
title: Themes
subtitle: Browse the archive by recurring ideas
permalink: /themes/
---

# Themes

Use these themes as fast catalog entry points. Each item routes into [search](/search/) with the theme prefilled.

<div class="term-cloud">
{% for theme in site.data.taxonomies.themes %}
  <a class="term-chip" href="/search/?q={{ theme | uri_escape }}">{{ theme }}</a>
{% endfor %}
</div>

## Notes

- Themes are intentionally compact and archival.
- They are navigation handles first, not essays.
- `limited-government` and related tags will expand as the catalog grows.

## Portuguese (pt-BR)
Indice tematico para navegar por ideias recorrentes do acervo.
