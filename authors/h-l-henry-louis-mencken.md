---
layout: page
title: "H. L. (Henry Louis) Mencken"
subtitle: "Author represented in the liberal archive"
permalink: /authors/h-l-henry-louis-mencken/
author_key: h-l-henry-louis-mencken
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
