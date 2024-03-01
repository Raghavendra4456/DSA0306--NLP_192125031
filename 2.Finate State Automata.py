class EndsWithABAutomaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'a', 'b'}
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q2'},
            'q2': {'a': 'q1', 'b': 'q0'}
        }
        self.current_state = 'q0'
    def process_input(self, input_string):
        for symbol in input_string:
            if symbol not in self.alphabet:
                print(f"Invalid symbol '{symbol}' in the input.")
                return False
            self.current_state = self.transitions[self.current_state][symbol]
        return self.current_state == 'q2'
def main():
    automaton = EndsWithABAutomaton()
    test_strings = ['aaaab', 'xyzab', 'ab', 'aab', 'bbab']
    for test_string in test_strings:
        result = automaton.process_input(test_string)
        if result:
            print(f"'{test_string}' matches the pattern.")
        else:
            print(f"'{test_string}' does not match the pattern.")
if __name__ == "__main__":
    main()
