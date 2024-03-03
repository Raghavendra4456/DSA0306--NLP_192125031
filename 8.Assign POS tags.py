import random
def train_pos_tagger(training_data):
    pos_model = {}
    for sentence in training_data:
        for word, pos_tag in sentence:
            if pos_tag not in pos_model:
                pos_model[pos_tag] = {}
            if word not in pos_model[pos_tag]:
                pos_model[pos_tag][word] = 1
            else:
                pos_model[pos_tag][word] += 1
    return pos_model
def stochastic_pos_tagging(sentence, pos_model):
    tagged_sentence = []
    for word in sentence:
        if word in pos_model:
            pos_probabilities = pos_model[word]
            most_probable_pos = max(pos_probabilities, key=pos_probabilities.get)
            tagged_sentence.append((word, most_probable_pos))
        else:
            tagged_sentence.append((word, 'UNKNOWN'))
    return tagged_sentence
training_data = [
    [("The", "DT"), ("cat", "NN"), ("is", "VBZ"), ("on", "IN"), ("the", "DT"), ("mat", "NN")],
    [("A", "DT"), ("quick", "JJ"), ("brown", "JJ"), ("fox", "NN"), ("jumps", "VBZ"), ("over", "IN"), ("the", "DT"), ("lazy", "JJ"), ("dog", "NN")],
]
pos_model = train_pos_tagger(training_data)
test_sentence = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
tagged_sentence = stochastic_pos_tagging(test_sentence, pos_model)
print("Test Sentence:", " ".join(test_sentence))
print("Stochastic POS Tagging Result:", tagged_sentence)
