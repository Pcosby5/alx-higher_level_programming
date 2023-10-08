#!/usr/bin/python3
def multiple_returns(sentence):
    length_sentence = len(sentence)
    first_character = sentence[0]
    # check if string is empty
    if not sentence:
        return (0, None)
    return (length_sentence, first_character)
