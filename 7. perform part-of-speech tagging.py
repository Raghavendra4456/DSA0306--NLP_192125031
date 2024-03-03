import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
def pos_tagging(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    return pos_tags
text = "NLTK is a powerful library for natural language processing."
pos_tags_result = pos_tagging(text)
print("Original Text:", text)
print("\nPart-of-Speech Tags:")
for word, pos_tag in pos_tags_result:
    print(f"{word}: {pos_tag}")
