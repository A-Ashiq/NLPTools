from textacy import make_spacy_doc
from textacy.extract import pos_regex_matches


def detect_noun_phrases(sentence, return_as_string: bool = True):
    """Helps you infer what is being talked about in the sentence as
     noun phrases are useful for explaining the context of the sentence."""
    if return_as_string:
        return " ".join([chunk.text for chunk in sentence.noun_chunks])

    return [c for c in sentence.noun_chunks]


def detect_verb_phrases(sentence, return_as_string: bool = True):
    pattern = r"(<VERB>?<ADV>*<VERB>+)"
    doc = make_spacy_doc(data=sentence, lang="en_core_web_sm")
    verb_phrases = pos_regex_matches(doc=doc, pattern=pattern)
    if return_as_string:
        return " ".join([c.text for c in verb_phrases])
    return verb_phrases
