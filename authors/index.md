---
layout: page
title: Authors
subtitle: Indexed author pages
permalink: /authors/
wide-page: true
---

<p class="archive-kicker">Catalog index</p>
<p>Author pages work as compact sub-archives. Use them when you want a narrower shelf, a cleaner work list, or a biographical starting point before entering the texts.</p>

<ul class="author-grid">
{% for author in site.data.catalog.authors %}
  <li><a href="/authors/{{ author.slug }}/">{{ author.name }}</a></li>
{% endfor %}
</ul>

## Portuguese (pt-BR)
Indice de autores catalogados no site.
