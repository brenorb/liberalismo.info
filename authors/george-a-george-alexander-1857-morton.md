---
layout: page
title: "George A. (George Alexander) 1857- Morton"
subtitle: "Author represented in the liberal archive"
permalink: /authors/george-a-george-alexander-1857-morton/
author_key: george-a-george-alexander-1857-morton
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
