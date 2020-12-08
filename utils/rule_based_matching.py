from pydoc import Doc
from spacy.matcher import Matcher

from utils.nlp_document_parsing import NLP, open_as_nlp_document


def extract_full_names(nlp_document: Doc) -> list[str]:
    pattern = [{"POS": "PROPN"}, {"POS": "PROPN"}]
    matcher = Matcher(NLP.vocab)
    matcher.add("FULL_NAME", None, pattern)
    nlp_document = open_as_nlp_document(nlp_document)

    matches = matcher(nlp_document)

    return [nlp_document[start:end].text for _, start, end in matches]
