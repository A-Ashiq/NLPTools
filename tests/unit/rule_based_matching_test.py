import pytest

from utils.rule_based_matching import extract_full_names


@pytest.fixture()
def sentence_with_one_full_name():
    return "On Tuesday, Susie Jones decided it was time to get a christmas tree. "


@pytest.fixture()
def sentence_with_multiple_names(sentence_with_one_full_name):
    return f"{sentence_with_one_full_name}And on Thursday, she decided to meet her friend Kev Smith for a coffee. "


@pytest.fixture()
def sentence_with_no_names():
    return f"And on Thursday, Friday and Saturday. We chilled on Sunday. "


def test_extract_full_names_one_name_in_text(sentence_with_one_full_name):
    extracted_names = extract_full_names(sentence_with_one_full_name)
    assert len(extracted_names) == 1

    assert extracted_names[0] == "Susie Jones"


def test_extract_full_names_with_multiple_names_in_text(sentence_with_multiple_names):
    extracted_names = extract_full_names(sentence_with_multiple_names)
    assert len(extracted_names) == 2
    assert set(extracted_names) == {"Kev Smith", "Susie Jones"}


def test_extract_full_names_with_no_names_in_text(sentence_with_no_names):
    extract_names = extract_full_names(sentence_with_no_names)
    assert len(extract_names) == 0
