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


def test_build_work_markdown_uses_explicit_slug_when_provided():
    meta = WorkMetadata(
        title="On Liberty",
        author="John Stuart Mill",
        year_first_published=1859,
        original_language="en",
        source_url="https://example.org/on-liberty.txt",
        tags=["liberalism", "freedom"],
        source_format="txt",
        slug="mill-on-liberty",
    )
    work_input = WorkInput(
        metadata=meta,
        editorial_note="Public-domain edition used for archival study.",
        text_body="Liberty consists in doing what one desires.",
        source_credit="Project Gutenberg edition",
    )

    markdown = build_work_markdown(work_input)
    assert "permalink: /library/mill-on-liberty/" in markdown


def test_build_work_markdown_strips_project_gutenberg_boilerplate():
    meta = WorkMetadata(
        title="The Law",
        author="Frederic Bastiat",
        year_first_published=1850,
        original_language="fr",
        source_url="https://www.gutenberg.org/ebooks/44800",
        tags=["liberalism", "law"],
        source_format="txt",
    )
    work_input = WorkInput(
        metadata=meta,
        editorial_note="Primary-source transcription for archival use.",
        text_body="""
The Project Gutenberg eBook of The Law

Title: The Law

Author: Frédéric Bastiat

*** START OF THE PROJECT GUTENBERG EBOOK THE LAW ***

THE LAW

The law perverted! The law, and in its wake, the collective forces of the nation.

*** END OF THE PROJECT GUTENBERG EBOOK THE LAW ***
""",
        source_credit="Project Gutenberg edition",
    )

    markdown = build_work_markdown(work_input)
    assert "Project Gutenberg eBook" not in markdown
    assert "*** START OF THE PROJECT GUTENBERG EBOOK" not in markdown
    assert "*** END OF THE PROJECT GUTENBERG EBOOK" not in markdown
    assert "The law perverted!" in markdown


def test_build_work_markdown_strips_page_artifacts_and_extra_blank_lines():
    meta = WorkMetadata(
        title="On Liberty",
        author="John Stuart Mill",
        year_first_published=1859,
        original_language="en",
        source_url="https://example.org/on-liberty.txt",
        tags=["liberalism", "freedom"],
        source_format="txt",
    )
    work_input = WorkInput(
        metadata=meta,
        editorial_note="Cleaned text export.",
        text_body="""
{v}

Chapter I. Introductory

Liberty is the proper name of that condition.

{1}

The subject of this Essay is not the so-called Liberty of the Will.



{2}

But Civil, or Social Liberty.
""",
        source_credit="Public-domain transcription",
    )

    markdown = build_work_markdown(work_input)
    assert "{v}" not in markdown
    assert "{1}" not in markdown
    assert "{2}" not in markdown
    assert "\n\n\n" not in markdown
    assert "The subject of this Essay" in markdown
