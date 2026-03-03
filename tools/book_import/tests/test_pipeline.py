from book_import.pipeline import WorkInput, WorkMetadata, build_work_markdown, detect_chapters, make_slug


def test_make_slug_normalizes_title():
    assert make_slug("The Law (A Lei)") == "the-law-a-lei"
    assert make_slug("On Liberty!") == "on-liberty"


def test_detect_chapters_extracts_roman_and_numeric_headings():
    text = """
CHAPTER I. First Principles
Some text.

Chapter 2 - Property
More text.
"""
    chapters = detect_chapters(text)
    assert [chapter.title for chapter in chapters] == ["First Principles", "Property"]
    assert chapters[0].body.strip() == "Some text."
    assert chapters[1].body.strip() == "More text."


def test_build_work_markdown_matches_library_schema():
    meta = WorkMetadata(
        title="The Law",
        author="Frederic Bastiat",
        year_first_published=1850,
        original_language="fr",
        source_url="https://example.org/the-law.pdf",
        tags=["liberalism", "law"],
        source_format="pdf",
    )
    work_input = WorkInput(
        metadata=meta,
        editorial_note="Public-domain edition used for archival study.",
        text_body="Justice should protect liberty and property.",
        source_credit="Project Gutenberg edition",
    )

    markdown = build_work_markdown(work_input)
    assert markdown.startswith("---\nlayout: page\n")
    for required in (
        "title:",
        "author:",
        "year_first_published:",
        "original_language:",
        "source_url:",
        "tags:",
    ):
        assert required in markdown

    assert "## About the work" in markdown
    assert "## Editorial note" in markdown
    assert "## Primary source" in markdown
    assert "## Text" in markdown
    assert "Justice should protect liberty and property." in markdown
