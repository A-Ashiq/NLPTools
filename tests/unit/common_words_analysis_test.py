import pytest

from utils.common_words_analysis import find_n_most_common_words


@pytest.fixture()
def sentence_with_frequent_words():
    return "I like coffee, coffee is delicious and you can buy coffee everywhere in London. "


def test_common_words_analysis(sentence_with_frequent_words):
    counted_words = find_n_most_common_words(sentence_with_frequent_words, n=1)
    assert "Coffee", 3 == counted_words[0]
