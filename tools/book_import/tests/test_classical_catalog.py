from book_import.classical_catalog import build_catalog


def test_classical_catalog_has_scale_and_unique_slugs():
    catalog = build_catalog()
    works = catalog["works"]

    assert len(works) >= 500
    slugs = [work["slug"] for work in works]
    assert len(slugs) == len(set(slugs))


def test_classical_catalog_references_known_authors_and_sources():
    catalog = build_catalog()
    authors = {author["key"] for author in catalog["authors"]}

    for work in catalog["works"]:
        assert work["author_key"] in authors
        assert work["year_first_published"] > 0
        assert work["edition_language"] == "en"
        if work["mode"] == "fulltext":
            assert work["source_url"]
            assert work["source_text_url"]
