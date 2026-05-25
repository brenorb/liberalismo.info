---
layout: page
title: "William R. (William Rufus) 1886- Scott"
subtitle: "Author represented in the liberal archive"
permalink: /authors/william-r-william-rufus-1886-scott/
author_key: william-r-william-rufus-1886-scott
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
