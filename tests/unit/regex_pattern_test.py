import pytest

from utils.regex_patterns import search_text_for_pattern


@pytest.fixture()
def sample_file_path():
    return "/somedir/somesubdir/morepath"


def test_regex_lookup_for_file_path(sample_file_path):
    assert search_text_for_pattern(sample_file_path, pattern_type="file path")[0] == sample_file_path
