class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
    def parse(self, input_string):
        self.tokens = input_string.split()
        self.current_token = 0
        try:
            self.parse_start()
            print("Parsing successful!")
        except Exception as e:
            print(f"Parsing failed: {str(e)}")
    def match(self, expected_token):
        if self.current_token < len(self.tokens) and self.tokens[self.current_token] == expected_token:
            self.current_token += 1
        else:
            raise Exception(f"Expected '{expected_token}', found '{self.tokens[self.current_token]}'")
    def parse_start(self):
        self.parse_expression()
    def parse_expression(self):
        self.parse_term()
        self.parse_expression_tail()
    def parse_expression_tail(self):
        if self.current_token < len(self.tokens):
            if self.tokens[self.current_token] in ['+', '-']:
                self.match(self.tokens[self.current_token])
                self.parse_term()
                self.parse_expression_tail()
    def parse_term(self):
        self.parse_factor()
        self.parse_term_tail()
    def parse_term_tail(self):
        if self.current_token < len(self.tokens):
            if self.tokens[self.current_token] in ['*', '/']:
                self.match(self.tokens[self.current_token])
                self.parse_factor()
                self.parse_term_tail()
    def parse_factor(self):
        if self.current_token < len(self.tokens):
            if self.tokens[self.current_token].isdigit():
                self.match(self.tokens[self.current_token])
            elif self.tokens[self.current_token] == '(':
                self.match('(')
                self.parse_expression()
                self.match(')')
            else:
                raise Exception(f"Invalid token: {self.tokens[self.current_token]}")
grammar = """
    E -> T E'
    E' -> + T E' | ε
    T -> F T'
    T' -> * F T' | ε
    F -> ( E ) | num
"""
input_string = "( 3 + 5 ) * 2 - 4"
parser = Parser(grammar)
parser.parse(input_string)
