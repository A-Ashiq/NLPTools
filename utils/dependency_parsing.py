from spacy import displacy


def parse_sentence_for_dependencies(sentence) -> None:
    """Builds a visualisation for the dependency tree at http://127.0.0.1:5000"""
    return displacy.serve(sentence, style="dep")


def flatten_tree(tree) -> str:
    return ''.join([token.text_with_ws for token in list(tree)]).strip()
