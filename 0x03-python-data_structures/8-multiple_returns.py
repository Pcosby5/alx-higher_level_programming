#!/usr/bin/python3
def multiple_returns(sentence):
    # check if string is empty
    if not sentence:
        return (0, None)
    length_sentence = len(sentence)
    first_character = sentence[0]
    return (length_sentence, first_character)
