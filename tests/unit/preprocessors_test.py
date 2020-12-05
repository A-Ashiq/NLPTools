import pytest

from utils.preprocessors import lemmatize_functional_words


def test_lemmatize_words_extraction_works(sample_raw_string):
    lemmatized_words = lemmatize_functional_words(sample_raw_string)
    assert sample_raw_string == "Here is some sample text to be parsed. Apples are tasty and so is coffee. "
    assert lemmatized_words == ["sample", "text", "parse", "apple", "tasty", "coffee"]
