import re


REGEX_PATTERNS = {
    "file path": "(/[a-zA-Z\./_]*[\s]?)",
}


def search_text_for_pattern(text: str, pattern_type: str):
    regex_pattern = REGEX_PATTERNS.get(pattern_type)
    return re.findall(regex_pattern, text)
