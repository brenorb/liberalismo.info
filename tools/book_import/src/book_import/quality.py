from dataclasses import dataclass
import re
from collections import Counter

from rapidfuzz.distance import Levenshtein


@dataclass
class QualityReport:
    word_precision: float
    word_recall: float
    cer: float


def compare_texts(reference_text: str, candidate_text: str) -> QualityReport:
    ref_tokens = re.findall(r"[a-z0-9']+", reference_text.lower())
    cand_tokens = re.findall(r"[a-z0-9']+", candidate_text.lower())

    ref_counter = Counter(ref_tokens)
    cand_counter = Counter(cand_tokens)
    true_positives = sum(
        min(ref_counter[token], cand_counter[token]) for token in ref_counter.keys()
    )

    precision = true_positives / len(cand_tokens) if cand_tokens else 1.0
    recall = true_positives / len(ref_tokens) if ref_tokens else 1.0

    ref_norm = " ".join(ref_tokens)
    cand_norm = " ".join(cand_tokens)
    # Bound CER runtime for long books while keeping a meaningful sample.
    max_chars = 8000
    cer = Levenshtein.normalized_distance(ref_norm[:max_chars], cand_norm[:max_chars])

    return QualityReport(word_precision=precision, word_recall=recall, cer=cer)
