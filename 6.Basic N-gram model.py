import random
def create_bigram_model(text):
    words = text.split()
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    model = {}
    for word1, word2 in bigrams:
        if word1 in model:
            model[word1].append(word2)
        else:
            model[word1] = [word2]
    return model
def generate_text_bigram(model, length=10, start_word=None):
    if start_word is None:
        start_word = random.choice(list(model.keys()))
    current_word = start_word
    generated_text = [current_word]
    for _ in range(length - 1):
        if current_word in model:
            next_word = random.choice(model[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break
    return ' '.join(generated_text)
text_corpus = "This is a simple example of a bigram model for text generation. You can use it to generate short sentences."
bigram_model = create_bigram_model(text_corpus)
generated_text = generate_text_bigram(bigram_model, length=10)
print(generated_text)
