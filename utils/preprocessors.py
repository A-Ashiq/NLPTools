

def is_token_allowed(token) -> bool:
    """Only allow valid tokens which are not stop words or punctuation symbols."""
    if not token or not token.string.strip() or token.is_stop or token.is_punct:
        return False
    return True


def convert_token_to_lemma(token) -> str:
    """Reduces the token to it's lower case lemma form."""
    return token.lemma_.strip().lower()


def lemmatize_functional_words(complete_doc) -> list[str]:
    return [convert_token_to_lemma(token) for token in complete_doc if is_token_allowed(token)]
