#!/usr/bin/python3

"""Module to find the max integer in a list
"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The maximum integer in the list.

    If the list is empty, the function returns None.
    """
    # Check if the list is empty and return None if it is
    if len(list) == 0:
        return None

    # Initialize the result with the first element of the list
    result = list[0]
    count = 1

    # Iterate through the list to find the maximum value
    while count < len(list):
        if list[count] > result:
            result = list[count]
        count += 1

    return result
