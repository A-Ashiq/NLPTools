import pytest
from pathlib import Path


def file_finder(relative_path: str) -> Path:
    parent_dir = Path(__file__).resolve().parent
    return Path(fr'{parent_dir}/{relative_path}')


@pytest.fixture(scope="module")
def first_sample_txt_file_path() -> Path:
    return file_finder('sample_files/doc1.txt')
