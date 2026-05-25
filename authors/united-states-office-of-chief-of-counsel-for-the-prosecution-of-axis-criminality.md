---
layout: page
title: "United States. Office of Chief of Counsel for the Prosecution of Axis Criminality"
subtitle: "Author represented in the liberal archive"
permalink: /authors/united-states-office-of-chief-of-counsel-for-the-prosecution-of-axis-criminality/
author_key: united-states-office-of-chief-of-counsel-for-the-prosecution-of-axis-criminality
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
