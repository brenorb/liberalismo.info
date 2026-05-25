---
layout: page
title: "Dama Margaret Smith"
subtitle: "Author represented in the liberal archive"
permalink: /authors/dama-margaret-smith/
author_key: dama-margaret-smith
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
