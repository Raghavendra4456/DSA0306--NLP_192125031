from pyparsing import Word, alphas, infixNotation, opAssoc
identifier = Word(alphas)
variable = Word(alphas, exact=1)
quantifier = Word("∀∃", exact=1)
connective = Word("&|", exact=1)
negation = Word("~", exact=1)
expression = infixNotation(
    variable | identifier,
    [
        (negation, 1, opAssoc.RIGHT),
        (quantifier, 1, opAssoc.RIGHT),
        (connective, 2, opAssoc.LEFT),
    ]
)
def parse_fopc_expression(expr_str):
    try:
        parsed_expr = expression.parseString(expr_str, parseAll=True)[0]
        return parsed_expr
    except Exception as e:
        print(f"Error parsing expression: {e}")
        return None
if __name__ == "__main__":
    example_expression = "∀x (P(x) & Q(x))"
    parsed_result = parse_fopc_expression(example_expression)
    if parsed_result is not None:
        print("Parsed Result:")
        print(parsed_result)
