---
layout: page
title: Library
subtitle: Cataloged works
permalink: /library/
---

# Library

Use [search](/search/) to filter by author or tag, or browse [authors](/authors/).

## Works

<div class="signal-panel">
  <ul class="shelf-list">
{% for work in site.data.catalog.works %}
    <li><a href="{{ work.url }}">{{ work.title }}</a> <span class="shelf-meta">{{ work.author }}</span></li>
{% endfor %}
  </ul>
</div>

## Browse by theme

<div class="term-cloud">
{% for theme in site.data.taxonomies.themes %}
  <a class="term-chip" href="/search/?q={{ theme | uri_escape }}">{{ theme }}</a>
{% endfor %}
</div>

## Browse by school

<div class="term-cloud">
{% for school in site.data.taxonomies.schools %}
  <a class="term-chip" href="/search/?q={{ school | uri_escape }}">{{ school }}</a>
{% endfor %}
</div>

## Portuguese (pt-BR)
Biblioteca inicial com obras classicas, metadados estruturados e links de fonte primaria.
