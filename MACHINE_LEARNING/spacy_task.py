import spacy


nlp = spacy.load("en_core_web_sm")

def process_text(text):
    doc = nlp(text)
    result = []
    for token in doc:
        result.append({
            "text": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "tag": token.tag_,
            "dep": token.dep_,
            "head": token.head.text
        })
    return result
