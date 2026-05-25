---
layout: page
title: Search
subtitle: Search by work, author, or tag
permalink: /search/
---

<input id="search-input" type="text" placeholder="Search by title, author, or tag" style="width:100%;padding:10px;margin-bottom:16px;">
<div id="search-results"></div>

<script>
(async function () {
  const input = document.getElementById('search-input');
  const results = document.getElementById('search-results');
  const data = await fetch('/search.json').then(r => r.json());
  const params = new URLSearchParams(window.location.search);

  function render(items) {
    if (!items.length) {
      results.innerHTML = '<p>No results.</p>';
      return;
    }
    results.innerHTML = items.map(item => {
      return `<article style="margin-bottom:18px;">
        <h3 style="margin:0 0 6px;"><a href="${item.url}">${item.title}</a></h3>
        <p style="margin:0 0 4px;"><strong>Author:</strong> ${item.author}</p>
        <p style="margin:0;color:#555;">${item.excerpt}</p>
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
