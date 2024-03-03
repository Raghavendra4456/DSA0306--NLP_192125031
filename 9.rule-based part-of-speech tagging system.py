import re
def rule_based_pos_tagging(sentence):
    tagged_sentence = []
    for word in sentence:
        if re.match(r'\b(?:the|a|an)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'DT'))  # Determiner
        elif re.match(r'\b(?:is|am|are|was|were)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'VB'))  # Verb
        elif re.match(r'\b(?:cat|dog|fox)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'NN'))  # Noun
        elif re.match(r'\b(?:quick|brown|lazy)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'JJ'))  # Adjective
        elif re.match(r'\b(?:over|on|in)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'IN'))  # Preposition
        else:
            tagged_sentence.append((word, 'UNKNOWN'))  # Default
    return tagged_sentence
test_sentence = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
tagged_sentence = rule_based_pos_tagging(test_sentence)
print("Test Sentence:", " ".join(test_sentence))
print("Rule-Based POS Tagging Result:", tagged_sentence)
