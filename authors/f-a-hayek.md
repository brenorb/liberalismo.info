---
layout: page
title: "F. A. Hayek"
subtitle: "Austrian-British theorist of spontaneous order and rule-based liberty"
permalink: /authors/f-a-hayek/
author_key: f-a-hayek
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
