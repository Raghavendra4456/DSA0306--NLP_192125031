class PluralStateMachine:
    def __init__(self):
        self.states = {'start', 'add_s', 'add_es'}
        self.transitions = {
            'start': {'noun': 'add_s'},
            'add_s': {'noun': 'add_es'},
            'add_es': {'noun': 'add_es'}
        }
        self.current_state = 'start'
    def process_noun(self, noun):
        for char in noun:
            if char.isalpha():
                self.current_state = self.transitions[self.current_state]['noun']
        if self.current_state == 'add_s':
            return noun + 's'
        elif self.current_state == 'add_es':
            return noun + 'es'
        else:
            return "Invalid noun"
def main():
    plural_machine = PluralStateMachine()
    nouns_to_pluralize = ['cat', 'dog', 'house', 'child']
    for noun in nouns_to_pluralize:
        plural_form = plural_machine.process_noun(noun)
        print(f"The plural form of '{noun}' is '{plural_form}'")
if __name__ == "__main__":
    main()
