from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable


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


@dataclass
class WorkInput:
    metadata: WorkMetadata
    editorial_note: str
    text_body: str
    source_credit: str


def make_slug(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return re.sub(r"-{2,}", "-", slug)


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
    normalized = re.sub(r"(\w)-\n(\w)", r"\1\2", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def build_work_markdown(work_input: WorkInput) -> str:
    meta = work_input.metadata
    slug = make_slug(meta.title)
    body_text = _clean_text(work_input.text_body)
    chapters = detect_chapters(body_text)

    lines = [
        "---",
        "layout: page",
        f'title: "{meta.title}"',
        f'subtitle: "{meta.author}"',
        f"permalink: /library/{slug}/",
        f"author: {meta.author}",
        f"original_language: {meta.original_language}",
        f"year_first_published: {meta.year_first_published}",
        f'source_url: "{meta.source_url}"',
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
