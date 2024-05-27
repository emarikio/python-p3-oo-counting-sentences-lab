#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Use the property setter to assign the value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):  # Verify if the new value is a string
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Split the value using regular expression to match periods, question marks, and exclamation marks
        sentences = re.split(r'[.!?]+', self._value)
        # Remove empty strings from the list
        sentences = [sentence for sentence in sentences if sentence]
        return len(sentences)