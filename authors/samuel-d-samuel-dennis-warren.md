---
layout: page
title: "Samuel D. (Samuel Dennis) Warren"
subtitle: "Author represented in the liberal archive"
permalink: /authors/samuel-d-samuel-dennis-warren/
author_key: samuel-d-samuel-dennis-warren
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
