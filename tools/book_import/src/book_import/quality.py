from dataclasses import dataclass


@dataclass
class QualityReport:
    word_precision: float
    word_recall: float
    cer: float


def compare_texts(reference_text: str, candidate_text: str) -> QualityReport:
    raise NotImplementedError

