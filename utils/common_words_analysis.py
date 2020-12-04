from collections import Counter

from utils.setup import nlp


def find_n_most_common_words(text: str, n: int = 5):
    doc = nlp(text)

    words = [token.text for token in doc if not token.is_stop and not token.is_punct]

    return Counter(words).most_common(n)
