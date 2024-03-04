class ParseTreeNode:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []
    def __str__(self, level=0):
        tree_str = "\t" * level + f"{self.label}\n"
        for child in self.children:
            tree_str += child.__str__(level + 1)
        return tree_str
class EarleyParserWithParseTree:
    def __init__(self, grammar):
        self.grammar = grammar
        self.parse_tree = None
    def parse(self, input_string):
        chart = [set() for _ in range(len(input_string) + 1)]
        self.predict(0, chart)
        for i in range(len(input_string) + 1):
            self.scan(i, input_string, chart)
            for j in range(len(chart[i])):
                rule = chart[i].pop()
                self.complete(i, rule, chart)
        return self.accept(chart, input_string)
    def predict(self, index, chart):
        for rule in self.grammar:
            if rule[1] is not None:
                chart[index].add((rule, 0, index))
    def scan(self, index, input_string, chart):
        for rule in chart[index]:
            if rule[0][1] is not None and rule[0][1] == input_string[index-1]:
                chart[index].add((rule[0], rule[1]+1, rule[2]))
    def complete(self, index, rule, chart):
        for r in chart[rule[2]]:
            if r[0][1] is not None and r[0][1] == rule[0][0] and r[1] == rule[0][2]:
                chart[index].add((r[0], r[1]+1, r[2]))
    def accept(self, chart, input_string):
        for rule in chart[-1]:
            if rule[0][0] == 'S' and rule[1] == 1 and rule[2] == 0:
                self.construct_parse_tree(chart, input_string)
                return True
        return False
    def construct_parse_tree(self, chart, input_string):
        start_rule = None
        for rule in chart[-1]:
            if rule[0][0] == 'S' and rule[1] == 1 and rule[2] == 0:
                start_rule = rule
                break
        if start_rule:
            self.parse_tree = self.build_tree(start_rule, chart)
    def build_tree(self, rule, chart):
        label, expansion, origin = rule[0]
        if len(expansion) == 1 and expansion[0] is not None:
            return ParseTreeNode(label, [ParseTreeNode(expansion[0])])
        children = []
        for child_rule in chart[origin]:
            if child_rule[0] == (expansion[0], None) and child_rule[1] == 1 and child_rule[2] == origin + 1:
                children.append(self.build_tree(child_rule, chart))
        return ParseTreeNode(label, children)
grammar = [
    ('S', ['NP', 'VP']),
    ('NP', ['Det', 'N']),
    ('VP', ['V', 'NP']),
    ('Det', ['the']),
    ('N', ['cat']),
    ('V', ['chased']),
]
parser = EarleyParserWithParseTree(grammar)
input_string = 'the cat chased'
result = parser.parse(input_string.split())
if result:
    parse_tree = parser.parse_tree
    print(f'The parse tree for the input string "{input_string}" is:')
    print(parse_tree)
else:
    print(f'The input string "{input_string}" is not valid according to the grammar.')
