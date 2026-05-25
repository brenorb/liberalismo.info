---
layout: page
title: "Thomas (Thomas Herman Anthonius Maria) 1954- Cool"
subtitle: "Author represented in the liberal archive"
permalink: /authors/thomas-thomas-herman-anthonius-maria-1954-cool/
author_key: thomas-thomas-herman-anthonius-maria-1954-cool
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
