from pathlib import Path

from book_import import extractors


def test_extract_pdf_falls_back_to_ocr_when_text_layer_fails(monkeypatch, tmp_path):
    pdf_path = tmp_path / "sample.pdf"
    pdf_path.write_bytes(b"%PDF-1.4")

    def raise_read_error(_: Path) -> str:
        raise RuntimeError("bad pdf xref")

    monkeypatch.setattr(extractors, "_extract_pdf_text_layer", raise_read_error)
    monkeypatch.setattr(extractors, "_extract_pdf_ocr", lambda *_args, **_kwargs: "ocr text")

    result = extractors._extract_pdf(
        pdf_path,
        force_ocr=False,
        ocr_language="eng",
        ocr_pages=None,
    )

    assert result.strategy == "pdf-ocr"
    assert result.text == "ocr text"


def test_extract_text_strips_utf8_bom(tmp_path):
    txt_path = tmp_path / "sample.txt"
    txt_path.write_text("\ufeffLiberty lives.", encoding="utf-8")

    result = extractors.extract_text(txt_path)
    assert result.text == "Liberty lives."
