from typing import Union
from pathlib import Path

from spacy.tokens import Doc
from spacy import load as spacy_load
from spacy import lang


NLP = spacy_load('en_core_web_sm')


def open_file_as_nlp_document(file_path: str) -> Doc:
    with open(file_path, 'r') as f:
        return NLP(f.read())


def open_as_nlp_document(text: Union[Doc, Path, str]):
    if type(text) is Doc:
        return text
    try:
        return open_file_as_nlp_document(text)
    except FileNotFoundError:
        return NLP(text)


def filter_sentence_for_interesting_words(sentence) -> list[str]:
    return [token.text for token in sentence
            if not token.is_stop
            if not token.is_punct
            if not token.is_space
            if token.tag_ in ('NNP', 'NN')
            ]


def stop_words() -> list[str]:
    return lang.en.stop_words.STOP_WORDS
