import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
def explore_word_meanings(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        print(f"No synsets found for '{word}'.")
        return
    print(f"Synsets for '{word}':")
    for synset in synsets:
        print(f"\nSynset: {synset.name()}")
        print(f"POS (Part of Speech): {synset.pos()}")
        print(f"Definition: {synset.definition()}")
        print("Lemmas:")
        for lemma in synset.lemmas():
            print(f" - {lemma.name()}")
        hypernyms = synset.hypernyms()
        if hypernyms:
            print("\nHypernyms:")
            for hypernym in hypernyms:
                print(f" - {hypernym.name()}")
        hyponyms = synset.hyponyms()
        if hyponyms:
            print("\nHyponyms:")
            for hyponym in hyponyms:
                print(f" - {hyponym.name()}")
        print("\n---------------------")
if __name__ == "__main__":
    example_word = "dog"
    explore_word_meanings(example_word)
