from pydoc import Doc
from spacy.matcher import Matcher

from utils.nlp_document_parsing import NLP, open_as_nlp_document


RULE_BASED_PATTERNS = {
    "FULL NAME": [{"POS": "PROPN"}, {"POS": "PROPN"}],
    "PHONE NUMBER": [{'ORTH': '+'}, {'SHAPE': 'ddd'},]
}


def _extract_entity(entity, nlp_document) -> list[str]:
    entity = entity.upper()
    pattern = RULE_BASED_PATTERNS.get(entity)
    matcher = Matcher(NLP.vocab)
    matcher.add(entity, None, pattern)

    nlp_document = open_as_nlp_document(nlp_document)
    matches = matcher(nlp_document)

    return [nlp_document[start:end].text for _, start, end in matches]


def extract_full_names(nlp_document: Doc) -> list[str]:
    return _extract_entity(entity="FULL NAME", nlp_document=nlp_document)


def extract_phone_number(nlp_document):
    return _extract_entity("PHONE NUMBER", nlp_document)
