from typing import Any
from collections import Counter

from utils.nlp_document_parsing import open_as_nlp_document


def find_n_most_common_words(text: str, n: int = 5) -> list[tuple[Any, int]]:
    text = open_as_nlp_document(text)
    words = [token.text for token in text if not token.is_stop and not token.is_punct]

    return Counter(words).most_common(n)
