class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar
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
                return True
        return False
grammar = [
    ('S', ['NP', 'VP']),
    ('NP', ['Det', 'N']),
    ('VP', ['V', 'NP']),
    ('Det', ['the']),
    ('N', ['cat']),
    ('V', ['chased']),
]
parser = EarleyParser(grammar)
input_string = 'the cat chased'
result = parser.parse(input_string.split())
if result:
    print(f'The input string "{input_string}" is valid according to the grammar.')
else:
    print(f'The input string "{input_string}" is not valid according to the grammar.')
