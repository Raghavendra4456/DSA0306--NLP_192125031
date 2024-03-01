import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('wordnet')
def morphological_analysis(word):
    tokens = word_tokenize(word)
    pos_tags = nltk.pos_tag(tokens)
    print("Part-of-Speech Tags:")
    for token, pos_tag in pos_tags:
        print(f"{token}: {pos_tag}")
    print("\nMorphological Analysis using WordNet:")
    for token, pos_tag in pos_tags:
        synsets = wordnet.synsets(token)
        if synsets:
            print(f"{token}: {', '.join(set(lemma.name() for synset in synsets for lemma in synset.lemmas()))}")
        else:
            print(f"{token}: No information available in WordNet")
def main():
    example_word = "running"
    morphological_analysis(example_word)
if __name__ == "__main__":
    main()
