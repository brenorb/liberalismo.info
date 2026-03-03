from __future__ import annotations

from pathlib import Path

import click

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
