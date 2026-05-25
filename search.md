---
layout: page
title: Search
subtitle: Search by work, author, or tag
permalink: /search/
hide-page-hero: true
wide-page: true
surfaceless: true
---

<div class="search-shell">
  <section class="search-hero">
    <p class="archive-kicker">Catalog query</p>
    <h1 class="library-display">Search the archive like a shelf, not a feed.</h1>
    <p class="library-lead">Query by title, author, tag, or excerpt. The result set stays intentionally plain, quiet, and scan-friendly.</p>
  </section>

  <section class="search-console">
    <input id="search-input" type="text" placeholder="Search by title, author, or tag">
    <div id="search-results"></div>
  </section>
</div>

<script>
(async function () {
  const input = document.getElementById('search-input');
  const results = document.getElementById('search-results');
  const data = await fetch('/search.json').then(r => r.json());
  const params = new URLSearchParams(window.location.search);

  function render(items) {
    if (!items.length) {
      results.innerHTML = '<p class="search-empty">No results.</p>';
      return;
    }
    results.innerHTML = items.map(item => {
      return `<article class="search-hit">
        <p class="micro-meta">Catalog hit</p>
        <h3><a href="${item.url}">${item.title}</a></h3>
        <p class="search-hit-meta"><strong>Author:</strong> ${item.author}</p>
        <p class="search-hit-excerpt">${item.excerpt}</p>
      </article>`;
    }).join('');
  }

  function query(value) {
    const q = value.toLowerCase().trim();
    if (!q) {
      history.replaceState(null, '', window.location.pathname);
      render(data);
      return;
    }
    history.replaceState(null, '', `${window.location.pathname}?q=${encodeURIComponent(value)}`);
    const filtered = data.filter(item => {
      return (
        item.title.toLowerCase().includes(q) ||
        item.author.toLowerCase().includes(q) ||
        item.tags.toLowerCase().includes(q) ||
        item.excerpt.toLowerCase().includes(q)
      );
    });
    render(filtered);
  }

  input.addEventListener('input', e => query(e.target.value));
  input.value = params.get('q') || '';
  query(input.value);
})();
</script>

## Portuguese (pt-BR)
Use a busca para encontrar obras por titulo, autor ou tema.
