---
layout: page
title: Library
subtitle: Cataloged works
permalink: /library/
---

{% assign work_count = site.data.catalog.works | size %}
{% assign fulltext_count = site.data.catalog.works | where: "mode", "fulltext" | size %}
{% assign catalog_count = work_count | minus: fulltext_count %}

# Library

<div class="library-shell">
  <section class="library-heading">
    <div>
      <p class="archive-kicker">Open catalog</p>
      <h1 class="library-display">A long shelf of liberal works.</h1>
      <p class="library-lead">Use <a href="/search/">search</a> when you know the concept, or scan the shelf directly when you want range and surprise.</p>
    </div>
    <div class="archive-stats">
      <div class="archive-stat">
        <span class="archive-stat-label">Total works</span>
        <strong>{{ work_count }}</strong>
      </div>
      <div class="archive-stat">
        <span class="archive-stat-label">Hosted full text</span>
        <strong>{{ fulltext_count }}</strong>
      </div>
      <div class="archive-stat">
        <span class="archive-stat-label">Catalog references</span>
        <strong>{{ catalog_count }}</strong>
      </div>
    </div>
  </section>

  <section class="signal-panel">
    <p class="archive-kicker">Works</p>
    <ul class="shelf-list shelf-list-dense">
{% for work in site.data.catalog.works %}
      <li><a href="{{ work.url }}">{{ work.title }}</a> <span class="shelf-meta">{{ work.author }}</span> <span class="shelf-mode">{{ work.mode }}</span></li>
{% endfor %}
    </ul>
  </section>

  <section class="archive-columns">
    <article class="signal-panel">
      <p class="archive-kicker">Browse by theme</p>
      <div class="term-cloud">
{% for theme in site.data.taxonomies.themes %}
        <a class="term-chip" href="/search/?q={{ theme | uri_escape }}">{{ theme }}</a>
{% endfor %}
      </div>
    </article>

    <article class="signal-panel">
      <p class="archive-kicker">Browse by school</p>
      <div class="term-cloud">
{% for school in site.data.taxonomies.schools %}
        <a class="term-chip" href="/search/?q={{ school | uri_escape }}">{{ school }}</a>
{% endfor %}
      </div>
    </article>
  </section>
</div>

## Portuguese (pt-BR)
Biblioteca ampliada com um catalogo longo, um nucleo pequeno de texto integral hospedado no site e referencias bibliograficas para o restante da colecao.
