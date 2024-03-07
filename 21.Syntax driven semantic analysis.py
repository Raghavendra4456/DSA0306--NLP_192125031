import spacy
def extract_noun_phrases(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    noun_phrases = []
    for chunk in doc.noun_chunks:
        noun_phrase = {
            'text': chunk.text,
            'root_text': chunk.root.text,
            'root_pos': chunk.root.pos_,
            'root_dep': chunk.root.dep_,
            'meaning': get_meaning(chunk.root)
        }
        noun_phrases.append(noun_phrase)
    return noun_phrases
def get_meaning(word):
    meanings = [sense.definition() for sense in word._.wordnet.synsets()]
    return meanings if meanings else None
if __name__ == "__main__":
    example_sentence = "The quick brown fox jumps over the lazy dog."
    extracted_phrases = extract_noun_phrases(example_sentence)
    print("Noun Phrases and Meanings:")
    for phrase in extracted_phrases:
        print(f"{phrase['text']} ({phrase['root_pos']} - {phrase['root_dep']}): {phrase['meaning']}")
