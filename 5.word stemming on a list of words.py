import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
def perform_stemming(words):
    porter_stemmer = PorterStemmer()
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    return stemmed_words
def main():
    words_to_stem = ["running", "flies", "happily", "agreed", "better", "quickly"]
    stemmed_words = perform_stemming(words_to_stem)
    for original, stemmed in zip(words_to_stem, stemmed_words):
        print(f"Original: {original}\t\tStemmed: {stemmed}")
if __name__ == "__main__":
    main()
