"""Named Entity Recognition is the process of locating named entities in unstructured text and then
classifying them into pre-defined categories, such as person names, organizations, locations, monetary values,
percentages, time expressions etc."""

from utils.nlp_document_parsing import open_as_nlp_document


def _redact_person_names(token) -> str:
    if token.ent_iob != 0 and token.ent_type_ == "PERSON":
        return "[REDACTED]"
    return token.string


def merge_entity_spans(nlp_document) -> None:
    with nlp_document.retokenize() as retokenizer:
        for entity in nlp_document.ents:
            retokenizer.merge(entity)


def redact_names(nlp_document) -> str:
    nlp_document = open_as_nlp_document(nlp_document)
    merge_entity_spans(nlp_document)
    return " ".join((_redact_person_names(x) for x in nlp_document))
