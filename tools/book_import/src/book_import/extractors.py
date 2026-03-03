from __future__ import annotations

from dataclasses import dataclass
import tempfile
from pathlib import Path
import re
from typing import Callable
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from ebooklib import ITEM_DOCUMENT, epub
from pypdf import PdfReader
import requests


@dataclass
class ExtractionResult:
    text: str
    strategy: str


def _normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.lstrip("\ufeff")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def download_source(url: str, destination_dir: Path) -> Path:
    parsed = urlparse(url)
    suffix = Path(parsed.path).suffix or ".bin"
    destination = destination_dir / f"downloaded-source{suffix}"
    response = requests.get(
        url,
        timeout=60,
        headers={"User-Agent": "liberalismo-book-import/0.1"},
    )
    response.raise_for_status()
    destination.write_bytes(response.content)
    return destination


def extract_text(
    source_path: Path,
    force_ocr: bool = False,
    ocr_language: str = "eng",
    ocr_pages: int | None = None,
) -> ExtractionResult:
    extension = source_path.suffix.lower()
    if extension in {".txt", ".md"}:
        return ExtractionResult(
            text=_normalize_text(source_path.read_text(encoding="utf-8", errors="ignore")),
            strategy="txt",
        )
    if extension in {".htm", ".html"}:
        return ExtractionResult(text=_extract_html(source_path), strategy="html")
    if extension == ".epub":
        return ExtractionResult(text=_extract_epub(source_path), strategy="epub")
    if extension == ".pdf":
        return _extract_pdf(source_path, force_ocr=force_ocr, ocr_language=ocr_language, ocr_pages=ocr_pages)

    raise ValueError(f"Unsupported extension: {extension}")


def prepare_source(source: str) -> tuple[Path, Callable[[], None]]:
    if re.match(r"^https?://", source):
        temp_dir = Path(tempfile.mkdtemp(prefix="book-import-"))
        local_file = download_source(source, temp_dir)

        def _cleanup() -> None:
            for entry in temp_dir.iterdir():
                entry.unlink(missing_ok=True)
            temp_dir.rmdir()

        return local_file, _cleanup

    path = Path(source).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Source file not found: {path}")
    return path, lambda: None


def _extract_html(source_path: Path) -> str:
    soup = BeautifulSoup(source_path.read_text(encoding="utf-8", errors="ignore"), "lxml")
    return _normalize_text(soup.get_text("\n"))


def _extract_epub(source_path: Path) -> str:
    book = epub.read_epub(str(source_path))
    parts: list[str] = []
    for item in book.get_items_of_type(ITEM_DOCUMENT):
        soup = BeautifulSoup(item.get_content(), "lxml-xml")
        text = soup.get_text("\n", strip=True)
        if text:
            parts.append(text)
    return _normalize_text("\n\n".join(parts))


def _extract_pdf(
    source_path: Path, force_ocr: bool, ocr_language: str, ocr_pages: int | None
) -> ExtractionResult:
    text = ""
    try:
        text = _extract_pdf_text_layer(source_path)
    except Exception:
        text = ""

    if text and not force_ocr and len(text.split()) >= 500:
        return ExtractionResult(text=_normalize_text(text), strategy="pdf-text-layer")

    ocr_text = _extract_pdf_ocr(source_path, ocr_language=ocr_language, ocr_pages=ocr_pages)
    if ocr_text.strip():
        return ExtractionResult(text=_normalize_text(ocr_text), strategy="pdf-ocr")

    if text:
        return ExtractionResult(text=_normalize_text(text), strategy="pdf-text-layer")

    raise RuntimeError(f"Could not extract text from PDF: {source_path}")


def _extract_pdf_text_layer(source_path: Path) -> str:
    reader = PdfReader(str(source_path))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n\n".join(pages)


def _extract_pdf_ocr(source_path: Path, ocr_language: str, ocr_pages: int | None) -> str:
    try:
        import fitz
        from PIL import Image
        import pytesseract
    except ModuleNotFoundError:
        return ""

    pages_text: list[str] = []
    try:
        with fitz.open(source_path) as doc:
            page_count = len(doc) if ocr_pages is None else min(len(doc), ocr_pages)
            for index in range(page_count):
                page = doc.load_page(index)
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
                image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                pages_text.append(pytesseract.image_to_string(image, lang=ocr_language))
    except Exception:
        return ""
    return "\n\n".join(pages_text)
