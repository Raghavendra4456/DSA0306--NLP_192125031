import spacy
def perform_ner(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
if __name__ == "__main__":
    example_text = "Apple Inc. was founded by Steve Jobs in Cupertino. It is a technology company."
    ner_results = perform_ner(example_text)
    print("Named Entities:")
    for entity, label in ner_results:
        print(f"{entity}: {label}")
