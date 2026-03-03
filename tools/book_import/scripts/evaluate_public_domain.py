#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import argparse
import json
import re

import requests

from book_import.extractors import extract_text, prepare_source
from book_import.pipeline import WorkInput, WorkMetadata, build_work_markdown, make_slug
from book_import.quality import compare_texts


@dataclass(frozen=True)
class SampleBook:
    key: str
    title: str
    author: str
    year_first_published: int
    original_language: str
    tags: list[str]
    source_url: str
    reference_url: str
    force_ocr: bool


SAMPLES: list[SampleBook] = [
    SampleBook(
        key="the-law-pdf-ocr",
        title="The Law",
        author="Frederic Bastiat",
        year_first_published=1850,
        original_language="fr",
        tags=["liberalism", "law", "state"],
        source_url="https://cdn.mises.org/thelaw.pdf",
        reference_url="https://www.gutenberg.org/cache/epub/44800/pg44800.txt",
        force_ocr=True,
    ),
    SampleBook(
        key="on-liberty-pdf-ocr",
        title="On Liberty",
        author="John Stuart Mill",
        year_first_published=1859,
        original_language="en",
        tags=["liberalism", "freedom", "society"],
        source_url="https://archive.org/download/onliberty00milluoft/onliberty00milluoft.pdf",
        reference_url="https://www.gutenberg.org/cache/epub/34901/pg34901.txt",
        force_ocr=True,
    ),
    SampleBook(
        key="wealth-of-nations-epub",
        title="The Wealth of Nations",
        author="Adam Smith",
        year_first_published=1776,
        original_language="en",
        tags=["economics", "classical-liberalism", "markets"],
        source_url="https://www.gutenberg.org/cache/epub/3300/pg3300-images-3.epub",
        reference_url="https://www.gutenberg.org/cache/epub/3300/pg3300.txt",
        force_ocr=False,
    ),
]


def fetch_text(url: str) -> str:
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    return response.text


def normalize_for_alignment(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate OCR/import quality on public-domain books.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("tools/book_import/out/imported"),
        help="Directory where generated markdown files are written.",
    )
    parser.add_argument(
        "--report-path",
        type=Path,
        default=Path("tools/book_import/out/ocr_report.md"),
        help="Markdown report output path.",
    )
    parser.add_argument(
        "--json-path",
        type=Path,
        default=Path("tools/book_import/out/ocr_report.json"),
        help="JSON report output path.",
    )
    parser.add_argument(
        "--ocr-language",
        default="eng",
        help="OCR language passed to Tesseract.",
    )
    parser.add_argument(
        "--ocr-pages",
        type=int,
        default=35,
        help="Max PDF pages to OCR per sample to keep runtime bounded.",
    )
    parser.add_argument(
        "--sample",
        action="append",
        default=[],
        help=f"Run only selected sample keys: {', '.join(sample.key for sample in SAMPLES)}",
    )
    args = parser.parse_args()

    selected = {key.strip() for key in args.sample if key.strip()}
    samples = [sample for sample in SAMPLES if not selected or sample.key in selected]

    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.report_path.parent.mkdir(parents=True, exist_ok=True)
    args.json_path.parent.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, object]] = []
    for sample in samples:
        local_source, cleanup = prepare_source(sample.source_url)
        try:
            extracted = extract_text(
                local_source,
                force_ocr=sample.force_ocr,
                ocr_language=args.ocr_language,
                ocr_pages=args.ocr_pages if sample.force_ocr else None,
            )
            extracted_tokens = normalize_for_alignment(extracted.text)
            reference_text = fetch_text(sample.reference_url)
            reference_tokens = normalize_for_alignment(reference_text)
            cutoff = min(len(reference_tokens), max(len(extracted_tokens), 1))
            aligned_reference = " ".join(reference_tokens[:cutoff])

            quality = compare_texts(aligned_reference, extracted.text)

            metadata = WorkMetadata(
                title=sample.title,
                author=sample.author,
                year_first_published=sample.year_first_published,
                original_language=sample.original_language,
                source_url=sample.source_url,
                tags=sample.tags,
                source_format=local_source.suffix.lower().lstrip("."),
            )
            work_input = WorkInput(
                metadata=metadata,
                editorial_note=(
                    "Auto-generated during OCR/import evaluation. "
                    "Review before publication."
                ),
                text_body=extracted.text,
                source_credit=f"Automated benchmark source [{extracted.strategy}]",
            )
            markdown = build_work_markdown(work_input)
            output_path = args.output_dir / f"{make_slug(sample.title)}.md"
            output_path.write_text(markdown)

            results.append(
                {
                    "sample": sample.key,
                    "title": sample.title,
                    "strategy": extracted.strategy,
                    "words_extracted": len(extracted_tokens),
                    "word_precision": round(quality.word_precision, 4),
                    "word_recall": round(quality.word_recall, 4),
                    "cer": round(quality.cer, 4),
                    "markdown_output": str(output_path),
                }
            )
        finally:
            cleanup()

    table_lines = [
        "# OCR and Import Evaluation",
        "",
        "Reference comparison uses a prefix-aligned slice with the same token count as extracted text.",
        "",
        "| Sample | Strategy | Words | Precision | Recall | CER | Markdown |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for result in results:
        table_lines.append(
            "| {sample} | {strategy} | {words_extracted} | {word_precision} | {word_recall} | {cer} | `{markdown_output}` |".format(
                **result
            )
        )

    args.report_path.write_text("\n".join(table_lines) + "\n")
    args.json_path.write_text(json.dumps(results, indent=2) + "\n")

    print(f"Wrote report: {args.report_path}")
    print(f"Wrote json:   {args.json_path}")


if __name__ == "__main__":
    main()
