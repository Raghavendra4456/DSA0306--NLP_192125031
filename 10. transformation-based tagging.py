import nltk
from nltk.tag import brill, untag
training_data = [
    [("The", "DT"), ("cat", "NN"), ("is", "VBZ"), ("on", "IN"), ("the", "DT"), ("mat", "NN")],
    [("A", "DT"), ("quick", "JJ"), ("brown", "JJ"), ("fox", "NN"), ("jumps", "VBZ"), ("over", "IN"), ("the", "DT"), ("lazy", "JJ"), ("dog", "NN")],
]
flat_training_data = [item for sublist in training_data for item in sublist]
def transformation_rules(tagged_words):
    rules = [
        brill.WordRule(r'^the$', ('DT',), 1),
        brill.WordRule(r'^a$', ('DT',), 1),
        brill.WordRule(r'^an$', ('DT',), 1),
        brill.WordRule(r'^is$', ('VB',), 1),
        brill.WordRule(r'^am$', ('VB',), 1),
        brill.WordRule(r'^are$', ('VB',), 1),
        brill.WordRule(r'^was$', ('VB',), 1),
        brill.WordRule(r'^were$', ('VB',), 1),
        brill.WordRule(r'^cat$', ('NN',), 1),
        brill.WordRule(r'^dog$', ('NN',), 1),
        brill.WordRule(r'^fox$', ('NN',), 1),
        brill.WordRule(r'^quick$', ('JJ',), 1),
        brill.WordRule(r'^brown$', ('JJ',), 1),
        brill.WordRule(r'^lazy$', ('JJ',), 1),
        brill.WordRule(r'^jumps$', ('VB',), 1),
        brill.WordRule(r'^over$', ('IN',), 1),
    ]
    template = brill.FastBrillTaggerTemplate(rules)
    trainer = brill.FastBrillTaggerTrainer(template)
    tagger = trainer.train([tagged_words], max_rules=10)
    return tagger.tag
transformed_tagger = transformation_rules(flat_training_data)
test_sentence = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
tagged_sentence = transformed_tagger(test_sentence)
print("Test Sentence:", " ".join(test_sentence))
print("Transformation-Based POS Tagging Result:", tagged_sentence)
