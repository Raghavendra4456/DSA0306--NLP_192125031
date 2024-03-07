import spacy
def perform_reference_resolution(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    antecedents = []
    pronouns = []
    for token in doc:
        if token.pos_ == 'NOUN':
            antecedents.append(token.text.lower())
        elif token.pos_ == 'PRON':
            pronouns.append(token.text.lower())
    resolved_text = text
    for pronoun in pronouns:
        antecedent = find_antecedent(pronoun, antecedents)
        if antecedent:
            resolved_text = resolved_text.replace(pronoun, antecedent, 1)
    return resolved_text
def find_antecedent(pronoun, antecedents):
    for antecedent in reversed(antecedents):
        if antecedent.lower() in pronoun.lower():
            return antecedent
    return None
if __name__ == "__main__":
    example_text = "The cat sat on the mat. It was fluffy."
    resolved_text = perform_reference_resolution(example_text)
    print("Original Text:")
    print(example_text)
    print("\nResolved Text:")
    print(resolved_text)
