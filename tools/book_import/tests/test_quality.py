from book_import.quality import compare_texts


def test_compare_texts_reports_perfect_match():
    result = compare_texts("Liberty and property.", "Liberty and property.")
    assert result.word_precision == 1.0
    assert result.word_recall == 1.0
    assert result.cer == 0.0


def test_compare_texts_detects_noisy_ocr_output():
    reference = "The law protects life, liberty, and property."
    candidate = "The taw protects life, hberty, and properfy."
    result = compare_texts(reference, candidate)
    assert result.word_recall < 1.0
    assert result.cer > 0.0
