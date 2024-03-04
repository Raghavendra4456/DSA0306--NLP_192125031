import nltk
from nltk import CFG, PCFG, ChartParser
from nltk.grammar import ProbabilisticProduction
def pcfg_parser(grammar, sentence):
    pcfg = PCFG.fromstring(grammar)
    parser = ChartParser(pcfg)
    parses = parser.parse(sentence.split())
    for tree in parses:
        print(tree)
        print(f'Probability: {tree.prob()}')
        print()
pcfg_grammar = """
    S -> NP VP [1.0]
    NP -> Det N [0.4] | NP PP [0.3] | 'John' [0.2] | 'I' [0.1]
    Det -> 'the' [0.6] | 'my' [0.4]
    N -> 'dog' [0.7] | 'cat' [0.3]
    VP -> V NP [0.5] | VP PP [0.5]
    V -> 'chased' [0.8] | 'saw' [0.2]
    PP -> P NP [1.0]
    P -> 'with' [0.6] | 'in' [0.4]
"""
sentence_to_parse = "I saw the dog with my cat"
pcfg_parser(pcfg_grammar, sentence_to_parse)
