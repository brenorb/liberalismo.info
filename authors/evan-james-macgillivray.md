---
layout: page
title: "Evan James MacGillivray"
subtitle: "Author represented in the liberal archive"
permalink: /authors/evan-james-macgillivray/
author_key: evan-james-macgillivray
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
