---
layout: page
title: "Harold W. (Harold Wellman) 1860- Fairbanks"
subtitle: "Author represented in the liberal archive"
permalink: /authors/harold-w-harold-wellman-1860-fairbanks/
author_key: harold-w-harold-wellman-1860-fairbanks
---
{% assign author = site.data.catalog.authors | where: "key", page.author_key | first %}

## Short bio
{{ author.bio }}

## Works on this site
{% assign works = site.data.catalog.works | where: "author_key", page.author_key %}
{% for work in works %}
- [{{ work.title }}](/library/{{ work.slug }}/)
{% endfor %}

## Portuguese (pt-BR)
{{ author.bio_pt_br }}
