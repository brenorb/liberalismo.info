---
layout: page
title: Schools
subtitle: Browse the archive by political-intellectual tradition
permalink: /schools/
wide-page: true
---

These schools provide a second entry point into the archive. Use them to branch by tradition rather than by single work.

<div class="term-cloud">
{% for school in site.data.taxonomies.schools %}
  <a class="term-chip" href="/search/?q={{ school | uri_escape }}">{{ school }}</a>
{% endfor %}
</div>

## Notes

- `classical-liberalism` is the present center of gravity.
- `libertarianism` and `austrian-school` are included because they share source adjacency with the broader archive.

## Portuguese (pt-BR)
Indice por escolas e tradicoes politicas relacionadas ao acervo.
