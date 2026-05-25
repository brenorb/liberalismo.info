---
layout: page
title: "Emperor of Rome Marcus Aurelius"
subtitle: "Author represented in the liberal archive"
permalink: /authors/emperor-of-rome-marcus-aurelius/
author_key: emperor-of-rome-marcus-aurelius
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
