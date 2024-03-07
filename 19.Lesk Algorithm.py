from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
def lesk_algorithm(context_sentence, target_word):
    context_tokens = word_tokenize(context_sentence.lower())
    stop_words = set(stopwords.words('english'))
    context_tokens = [token for token in context_tokens if token not in stop_words]
    target_senses = wordnet.synsets(target_word)
    if not target_senses:
        return None
    best_sense = None
    max_overlap = 0
    for sense in target_senses:
        sense_tokens = set(word_tokenize(sense.definition().lower()))
        sense_tokens.update(word_tokenize(' '.join(sense.examples()).lower()))
        overlap = len(set(context_tokens) & sense_tokens)
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense
    return best_sense
if __name__ == "__main__":
    example_sentence = "He saw the bank by the river."
    target_word = "bank"
    result_sense = lesk_algorithm(example_sentence, target_word)
    if result_sense:
        print(f"Target Word: {target_word}")
        print(f"Best Sense: {result_sense.name()}")
        print(f"Definition: {result_sense.definition()}")
    else:
        print(f"No suitable senses found for '{target_word}'.")
