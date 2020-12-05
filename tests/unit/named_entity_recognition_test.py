import pytest

from utils.named_entity_recognition import redact_names


@pytest.fixture()
def sentence_with_person_names():
    return "Out of 5 people surveyed, James Robert, Julie Fuller and Benjamin Brooks like apples. " \
           "Kelly Cox and Matthew Evans like oranges. "


@pytest.fixture()
def sentence_with_no_person_names():
    return "Out of 5 people surveyed, lots of people like apples and oranges. But everyone hates pears. "


def test_redact_names_works_with_multiple_names(sentence_with_person_names):
    assert "[REDACTED]" in redact_names(sentence_with_person_names)


def test_redact_names_does_not_redact_text_with_no_names(sentence_with_no_person_names):
    assert "[REDACTED]" not in redact_names(sentence_with_no_person_names)
