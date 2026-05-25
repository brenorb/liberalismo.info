---
layout: page
title: "Bernard 1873?- London"
subtitle: "Author represented in the liberal archive"
permalink: /authors/bernard-1873-london/
author_key: bernard-1873-london
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
