from __future__ import annotations

from dataclasses import dataclass
import json
import re
from typing import Iterable
import unicodedata


@dataclass
class Chapter:
    title: str
    body: str


@dataclass
class WorkMetadata:
    title: str
    author: str
    year_first_published: int
    original_language: str
    source_url: str
    tags: list[str]
    source_format: str
    edition_language: str = "en"
    slug: str | None = None


@dataclass
class WorkInput:
    metadata: WorkMetadata
    editorial_note: str
    text_body: str
    source_credit: str


def make_slug(title: str) -> str:
    normalized = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:80].rstrip("-")


def detect_chapters(text: str) -> list[Chapter]:
    lines = text.splitlines()
    chapter_pattern = re.compile(
        r"^(?:chapter|book|part)\s+((?:[ivxlcdm]+|\d+)[\.\-\:]?)\s*(?:[\.\-\:]\s*)?(.*)$",
        re.IGNORECASE,
    )

    hits: list[tuple[int, str, str]] = []
    for index, raw_line in enumerate(lines):
        line = raw_line.strip()
        if not line:
            continue
        match = chapter_pattern.match(line)
        if not match:
            continue
        raw_title = match.group(2).strip()
        title = raw_title or match.group(1).strip(".:- ")
        hits.append((index, match.group(1).strip(".:- "), title))

    if len(hits) < 2:
        return []

    chapters: list[Chapter] = []
    for i, (start, numeral, title) in enumerate(hits):
        next_start = hits[i + 1][0] if i + 1 < len(hits) else len(lines)
        body = "\n".join(lines[start + 1 : next_start]).strip()
        chapter_title = title or numeral
        if body:
            chapters.append(Chapter(title=chapter_title, body=body))

    return chapters


def _format_tags(tags: Iterable[str]) -> str:
    normalized = [tag.strip() for tag in tags if tag.strip()]
    return "[" + ", ".join(normalized) + "]"


def _clean_text(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = _strip_project_gutenberg_boilerplate(normalized)
    normalized = _strip_scanned_page_artifacts(normalized)
    normalized = re.sub(r"(\w)-\n(\w)", r"\1\2", normalized)
    normalized = re.sub(r"[ \t]+\n", "\n", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def _quote_yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _strip_project_gutenberg_boilerplate(text: str) -> str:
    start_pattern = re.compile(r"^\*\*\*\s*START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.*\*\*\*$", re.MULTILINE)
    end_pattern = re.compile(r"^\*\*\*\s*END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.*\*\*\*$", re.MULTILINE)

    start_match = start_pattern.search(text)
    if start_match:
      text = text[start_match.end() :]

    end_match = end_pattern.search(text)
    if end_match:
      text = text[: end_match.start()]

    return text


def _strip_scanned_page_artifacts(text: str) -> str:
    cleaned_lines: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if re.fullmatch(r"\{[ivxlcdm\d]+\}", line, re.IGNORECASE):
            continue
        cleaned_lines.append(raw_line)
    return "\n".join(cleaned_lines)


def build_work_markdown(work_input: WorkInput) -> str:
    meta = work_input.metadata
    slug = meta.slug or make_slug(meta.title)
    body_text = _clean_text(work_input.text_body)
    chapters = detect_chapters(body_text)

    lines = [
        "---",
        "layout: page",
        f"title: {_quote_yaml_string(meta.title)}",
        f"subtitle: {_quote_yaml_string(meta.author)}",
        f"permalink: /library/{slug}/",
        f"author: {meta.author}",
        f"original_language: {meta.original_language}",
        f"edition_language: {meta.edition_language}",
        f"year_first_published: {meta.year_first_published}",
        f"source_url: {_quote_yaml_string(meta.source_url)}",
        f"tags: {_format_tags(meta.tags)}",
        f"source_format: {meta.source_format}",
        "---",
        "",
        "## About the work",
        f"- Year: {meta.year_first_published}",
        f"- Author: {meta.author}",
        f"- Source format: {meta.source_format}",
        "- Editorial status: generated draft from source extraction",
        "",
        "## Editorial note",
        work_input.editorial_note.strip(),
        "",
        "## Primary source",
        (
            "Primary source used for this page: "
            f"{work_input.source_credit.strip()} ({meta.source_url})."
        ),
        "",
        "## Text",
    ]

    if chapters:
        lines.extend(["", "### Contents"])
        for chapter in chapters:
            lines.append(f"- {chapter.title}")
        for chapter in chapters:
            lines.extend(["", f"### {chapter.title}", "", chapter.body])
    else:
        lines.extend(["", body_text])

    lines.append("")
    return "\n".join(lines)
