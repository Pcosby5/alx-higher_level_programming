#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    new_dict = {}

    # Iterate through the key-value pairs in the input dictionary
    for key, value in a_dictionary.items():
        # Multiply the value by 2 and add it to the new dictionary
        new_dict[key] = value * 2

    return new_dict
