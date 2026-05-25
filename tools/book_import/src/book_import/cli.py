from __future__ import annotations

import json
from pathlib import Path

import click

from book_import.classical_catalog import build_catalog
from book_import.extractors import extract_text, prepare_source
from book_import.pipeline import WorkInput, WorkMetadata, build_work_markdown, make_slug


@click.group()
def main() -> None:
    """Book import commands for liberalismo.info."""


@main.command("ingest")
@click.option("--source", required=True, help="Path or URL to PDF/EPUB/HTML/TXT source.")
@click.option("--title", required=True, help="Book title.")
@click.option("--author", required=True, help="Book author.")
@click.option("--year", "year_first_published", type=int, required=True, help="First publication year.")
@click.option("--original-language", required=True, help="Language code, e.g., en, fr, pt.")
@click.option("--source-url", default="", help="Primary source URL for front matter.")
@click.option("--tags", required=True, help="Comma-separated tags.")
@click.option("--edition-language", default="", help="Language code for the hosted edition, e.g., en.")
@click.option(
    "--editorial-note",
    default="This page reproduces historical text for educational use.",
    show_default=True,
)
@click.option(
    "--source-credit",
    default="Imported source edition",
    show_default=True,
)
@click.option("--repo-root", type=click.Path(path_type=Path), default=Path.cwd(), show_default=True)
@click.option("--force-ocr", is_flag=True, help="Force OCR on PDF files.")
@click.option("--ocr-language", default="eng", show_default=True)
@click.option("--ocr-pages", type=int, default=None, help="Limit OCR pages for quicker runs.")
@click.option("--dry-run", is_flag=True, help="Print markdown instead of writing to disk.")
def ingest(
    source: str,
    title: str,
    author: str,
    year_first_published: int,
    original_language: str,
    source_url: str,
    tags: str,
    edition_language: str,
    editorial_note: str,
    source_credit: str,
    repo_root: Path,
    force_ocr: bool,
    ocr_language: str,
    ocr_pages: int | None,
    dry_run: bool,
) -> None:
    local_source, cleanup = prepare_source(source)
    try:
        source_reference = source_url.strip() or (source if source.startswith("http") else local_source.as_uri())
        extracted = extract_text(
            local_source,
            force_ocr=force_ocr,
            ocr_language=ocr_language,
            ocr_pages=ocr_pages,
        )
        metadata = WorkMetadata(
            title=title,
            author=author,
            year_first_published=year_first_published,
            original_language=original_language,
            edition_language=edition_language.strip() or original_language,
            source_url=source_reference,
            tags=[value.strip() for value in tags.split(",") if value.strip()],
            source_format=local_source.suffix.lower().lstrip("."),
        )
        work_input = WorkInput(
            metadata=metadata,
            editorial_note=editorial_note,
            text_body=extracted.text,
            source_credit=f"{source_credit} [{extracted.strategy}]",
        )
        markdown = build_work_markdown(work_input)
        if dry_run:
            click.echo(markdown)
            return

        output = repo_root / "library" / f"{make_slug(title)}.md"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown)
        click.echo(f"Wrote {output}")
    finally:
        cleanup()


AUTHOR_PAGE_TEMPLATE = """---
layout: page
title: "{name}"
subtitle: "{subtitle}"
permalink: /authors/{slug}/
author_key: {key}
---
{{% assign author = site.data.catalog.authors | where: "key", page.author_key | first %}}

## Short bio
{{{{ author.bio }}}}

## Works on this site
{{% assign works = site.data.catalog.works | where: "author_key", page.author_key %}}
{{% for work in works %}}
- [{{{{ work.title }}}}](/library/{{{{ work.slug }}}}/)
{{% endfor %}}

## Portuguese (pt-BR)
{{{{ author.bio_pt_br }}}}
"""


AUTHORS_INDEX_TEMPLATE = """---
layout: page
title: Authors
subtitle: Indexed author pages
permalink: /authors/
---

# Authors

{% for author in site.data.catalog.authors %}
- [{{ author.name }}](/authors/{{ author.slug }}/)
{% endfor %}

## Portuguese (pt-BR)
Indice de autores catalogados no site.
"""


REFERENCE_PAGE_TEMPLATE = """---
layout: page
title: {title}
subtitle: {author}
permalink: /library/{slug}/
author: {author}
original_language: {original_language}
edition_language: {edition_language}
year_first_published: {year_first_published}
source_url: {source_url}
tags: {tags}
source_format: catalog
---

## About the work
- Year: {year_first_published}
- Author: {author}
- Edition language: {edition_language}
- Source format: catalog
- Editorial status: bibliographic catalog entry

## Editorial note
This page records the work as part of the public catalog. Full text is not reproduced on this page.

## Source
Primary catalog source: Project Gutenberg metadata snapshot. Reading source: {source_url}

## Summary
{excerpt}

## Themes
{themes}
"""


GUIDE_PAGE_TEMPLATE = """---
layout: page
title: {title}
subtitle: {author}
permalink: /library/{slug}/
author: {author}
original_language: {original_language}
edition_language: {edition_language}
year_first_published: {year_first_published}
source_url: {source_url}
tags: {tags}
source_format: guide
---

## About the work
- Year: {year_first_published}
- Author: {author}
- Edition language: {edition_language}
- Source format: guide
- Editorial status: summary page for a still-copyrighted work

## Editorial note
This page records the work as part of the public catalog. The full text is not reproduced because the modern edition remains under copyright.

## Copyright status
This work is treated here as a guide entry only. Readers should consult the publisher or authorized editions for the full text.

## Source
Primary reading source: {source_url}

## Summary
{excerpt}

## Themes
{themes}
"""


def _format_frontmatter_tags(tags: list[str]) -> str:
    return "[" + ", ".join(tags) + "]"


def _yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def build_reference_markdown(work: dict[str, object]) -> str:
    themes = "\n".join(f"- {tag}" for tag in work["tags"])
    template = GUIDE_PAGE_TEMPLATE if work["mode"] == "guide" else REFERENCE_PAGE_TEMPLATE
    return template.format(
        title=_yaml_string(str(work["title"])),
        author=_yaml_string(str(work["author"])),
        slug=work["slug"],
        original_language=work["original_language"],
        edition_language=work["edition_language"],
        year_first_published=work["year_first_published"],
        source_url=_yaml_string(str(work["source_url"])),
        tags=_format_frontmatter_tags([str(tag) for tag in work["tags"]]),
        excerpt=work["excerpt"],
        themes=themes,
    )


@main.command("sync-classical-catalog")
@click.option("--repo-root", type=click.Path(path_type=Path), default=Path.cwd(), show_default=True)
@click.option("--limit", type=int, default=None, help="Only ingest the first N full-text works.")
def sync_classical_catalog(repo_root: Path, limit: int | None) -> None:
    catalog = build_catalog()
    authors_dir = repo_root / "authors"
    authors_dir.mkdir(parents=True, exist_ok=True)
    data_dir = repo_root / "_data"
    data_dir.mkdir(parents=True, exist_ok=True)
    library_dir = repo_root / "library"
    library_dir.mkdir(parents=True, exist_ok=True)

    for path in authors_dir.glob("*.md"):
        if path.name != "index.md":
            path.unlink()
    for path in library_dir.glob("*.md"):
        if path.name != "index.md":
            path.unlink()

    (data_dir / "catalog.json").write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (authors_dir / "index.md").write_text(AUTHORS_INDEX_TEMPLATE, encoding="utf-8")

    for author in catalog["authors"]:
        page = AUTHOR_PAGE_TEMPLATE.format(**author)
        (authors_dir / f"{author['slug']}.md").write_text(page, encoding="utf-8")

    fulltext_works = [work for work in catalog["works"] if work["mode"] == "fulltext"]
    if limit is not None:
        fulltext_works = fulltext_works[:limit]

    for work in fulltext_works:
        local_source, cleanup = prepare_source(str(work["source_text_url"]))
        try:
            extracted = extract_text(local_source)
            metadata = WorkMetadata(
                title=str(work["title"]),
                author=str(work["author"]),
                year_first_published=int(work["year_first_published"]),
                original_language=str(work["original_language"]),
                edition_language=str(work["edition_language"]),
                source_url=str(work["source_url"]),
                tags=[str(tag) for tag in work["tags"]],
                source_format=local_source.suffix.lower().lstrip("."),
                slug=str(work["slug"]),
            )
            markdown = build_work_markdown(
                WorkInput(
                    metadata=metadata,
                    editorial_note="This page reproduces historical text for educational use.",
                    text_body=extracted.text,
                    source_credit=f"Project Gutenberg edition [{extracted.strategy}]",
                )
            )
            output = library_dir / f"{work['slug']}.md"
            output.write_text(markdown, encoding="utf-8")
            click.echo(f"Wrote {output}")
        finally:
            cleanup()

    for work in catalog["works"]:
        if work["mode"] == "fulltext":
            continue
        output = library_dir / f"{work['slug']}.md"
        output.write_text(build_reference_markdown(work), encoding="utf-8")
        click.echo(f"Wrote {output}")
