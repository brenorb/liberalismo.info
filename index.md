---
layout: page
title: Liberalismo.info
subtitle: Open archive of liberal texts
use-site-title: false
hide-page-hero: true
wide-page: true
surfaceless: true
---

{% assign work_count = site.data.catalog.works | size %}
{% assign author_count = site.data.catalog.authors | size %}
{% assign fulltext_count = site.data.catalog.works | where: "mode", "fulltext" | size %}

<div class="archive-home">
  <section class="archive-masthead">
    <div class="archive-masthead-copy">
      <p class="archive-kicker">Public archive / English shelf / static publishing</p>
      <h1 class="archive-display">A liberal archive with <em>editorial calm</em> instead of template noise.</h1>
      <p class="archive-lead"><strong>Liberalismo.info</strong> is built as a research desk: primary texts, source-linked metadata, and direct routes into works, authors, themes, schools, reading paths, and search.</p>
    </div>
    <div class="archive-stats">
      <div class="archive-stat">
        <span class="archive-stat-label">Works</span>
        <strong>{{ work_count }}</strong>
      </div>
      <div class="archive-stat">
        <span class="archive-stat-label">Authors</span>
        <strong>{{ author_count }}</strong>
      </div>
      <div class="archive-stat">
        <span class="archive-stat-label">Full text</span>
        <strong>{{ fulltext_count }}</strong>
      </div>
    </div>
  </section>

  <section class="archive-board" aria-label="Browse the archive">
    <article class="archive-panel archive-panel-tall">
      <p class="micro-meta">Route 01</p>
      <h2><a href="/library/">Library</a></h2>
      <p>Scan all {{ work_count }} works as a disciplined catalog first, then drop into the smaller layer of hosted full text.</p>
    </article>
    <article class="archive-panel">
      <p class="micro-meta">Route 02</p>
      <h2><a href="/authors/">Authors</a></h2>
      <p>Use author pages as compact sub-archives with context, shelf lists, and consistent metadata.</p>
    </article>
    <article class="archive-panel">
      <p class="micro-meta">Route 03</p>
      <h2><a href="/themes/">Themes</a></h2>
      <p>Jump by recurring concerns like law, markets, institutions, democracy, freedom, and rights.</p>
    </article>
    <article class="archive-panel">
      <p class="micro-meta">Route 04</p>
      <h2><a href="/schools/">Schools</a></h2>
      <p>Map the shelf by tradition: classical liberalism, libertarianism, and the Austrian line.</p>
    </article>
    <article class="archive-panel archive-panel-wide">
      <p class="micro-meta">Route 05</p>
      <h2><a href="/docs/READING_PATHS/">Reading paths</a></h2>
      <p>Use sequenced entry points when you want a guided beginning instead of an unstructured cold start.</p>
    </article>
    <article class="archive-panel archive-panel-wide">
      <p class="micro-meta">Route 06</p>
      <h2><a href="/search/">Search</a></h2>
      <p>Query the catalog by author, work, tag, or excerpt when you already know the concept you need.</p>
    </article>
  </section>

  <section class="archive-columns">
    <article class="signal-panel">
      <p class="archive-kicker">Current shelf</p>
      <ul class="shelf-list">
      <li><a href="/library/the-law/">The Law</a> <span class="shelf-meta">Frederic Bastiat</span></li>
      <li><a href="/library/on-liberty/">On Liberty</a> <span class="shelf-meta">John Stuart Mill</span></li>
      <li><a href="/library/two-treatises/">Two Treatises of Government</a> <span class="shelf-meta">John Locke</span></li>
      <li><a href="/library/wealth-of-nations/">The Wealth of Nations</a> <span class="shelf-meta">Adam Smith</span></li>
      <li><a href="/library/road-to-serfdom/">The Road to Serfdom</a> <span class="shelf-meta">F. A. Hayek</span></li>
      <li><a href="/library/democracy-in-america/">Democracy in America</a> <span class="shelf-meta">Alexis de Tocqueville</span></li>
      </ul>
    </article>
    <article class="signal-panel">
      <p class="archive-kicker">Editorial stance</p>
      <ul class="archive-manifest">
        <li>Archive first: primary texts and durable metadata come before commentary layers.</li>
        <li>Static first: every page should stay plain, linkable, and easy to audit.</li>
        <li>Source linked: every work should point back to the edition or reference used.</li>
      </ul>
    </article>
  </section>
</div>

## Portuguese (pt-BR)

<div class="signal-panel">
  <p>O <strong>Liberalismo.info</strong> quer funcionar como um arquivo navegavel de textos do liberalismo: uma mesa editorial com rotas claras para obras, autores, temas, escolas, trilhas de leitura e documentacao.</p>
</div>
