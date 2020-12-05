from pathlib import PosixPath

import pytest
from spacy.tokens import Doc

from utils.nlp_document_parsing import open_as_nlp_document


@pytest.fixture()
def sample_raw_text():
    return "Here is some sample text to be parsed. Apples are tasty and so is coffee. "


def test_open_nlp_document_from_raw_text(sample_raw_text):
    nlp_document = open_as_nlp_document(sample_raw_text)
    assert type(nlp_document) is Doc
    assert nlp_document.text == sample_raw_text


def test_open_nlp_document_from_path_object(first_sample_txt_file_path):
    nlp_document = open_as_nlp_document(first_sample_txt_file_path)
    assert type(nlp_document) is Doc
    assert type(first_sample_txt_file_path) is PosixPath


def test_open_nlp_document_from_subsequent_nlp_doc_file(sample_raw_text):
    nlp_document = open_as_nlp_document(sample_raw_text)
    assert type(nlp_document) is Doc
    re_processed_nlp_document = open_as_nlp_document(nlp_document)
    assert type(re_processed_nlp_document) is Doc
