---
layout: page
title: Authors
subtitle: Indexed author pages
permalink: /authors/
---

# Authors

{% for author in site.data.catalog.authors %}
- [{{ author.name }}](/authors/{{ author.slug }}/)
{% endfor %}

## Portuguese (pt-BR)
Indice de autores catalogados no site.
