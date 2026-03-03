from dataclasses import dataclass


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
    raise NotImplementedError


def detect_chapters(text: str) -> list[Chapter]:
    raise NotImplementedError


def build_work_markdown(work_input: WorkInput) -> str:
    raise NotImplementedError

