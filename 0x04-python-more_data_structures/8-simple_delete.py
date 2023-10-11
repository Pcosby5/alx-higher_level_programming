#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Use the pop method with a default value of None to safely delete the key
    # If the key doesn't exist, no error is raised, and the dictionary remains unchanged
    a_dictionary.pop(key, None)

    return a_dictionary
