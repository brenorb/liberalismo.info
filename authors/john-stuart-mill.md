---
layout: page
title: "John Stuart Mill"
subtitle: "English liberal philosopher of liberty, individuality, and reform"
permalink: /authors/john-stuart-mill/
author_key: john-stuart-mill
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
