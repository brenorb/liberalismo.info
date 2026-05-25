---
layout: page
title: "Alexis de Tocqueville"
subtitle: "French analyst of democracy, civil society, and centralization"
permalink: /authors/alexis-de-tocqueville/
author_key: alexis-de-tocqueville
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
