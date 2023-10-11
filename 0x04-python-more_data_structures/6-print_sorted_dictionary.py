#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the sorted list of keys
    ordered_keys = sorted(a_dictionary.keys())

    # Iterate through the ordered keys and print the key-value pairs
    for key in ordered_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
