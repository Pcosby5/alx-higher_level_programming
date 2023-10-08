#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create a list comprehension that iterates through the elements in the input list.
    # The expression `not i & 1` is used to check if each element `i` is divisible by 2.
    # - `i & 1` performs a bitwise AND operation with 1, which effectively checks if the
    #   least significant bit of `i` is set (odd number) or not set (even number).
    # - `not i & 1` evaluates to True if `i` is even (not set) and False if `i` is odd (set).
    # The list comprehension creates a new list with True or False values for each element in the input list.
    return [not i & 1 for i in my_list]
