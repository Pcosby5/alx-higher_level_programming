#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    # Get the size of the input list
    size = len(list_of_integers)

    # Initialize variables for middle element and its index
    middle_e = size
    middle = size // 2

    # Check if the list is empty
    if size == 0:
        return None

    # Binary search for a peak
    while True:
        # Update the middle_e to be half of the current value
        middle_e = middle_e // 2

        # Check if there is a peak to the right
        if (middle < size - 1 and
                list_of_integers[middle] < list_of_integers[middle + 1]):
            if middle_e // 2 == 0:
                middle_e = 2
            middle = middle + middle_e // 2
        # Check if there is a peak to the left
        elif middle_e > 0 and list_of_integers[middle] < list_of_integers[middle - 1]:
            if middle_e // 2 == 0:
                middle_e = 2
            middle = middle - middle_e // 2
        # Found a peak
        else:
            return list_of_integers[middle]