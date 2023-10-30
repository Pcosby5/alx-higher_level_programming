#!/usr/bin/python3
"""

This module is composed by a function that prints a square with the character #

"""


def print_square(size):
    """ Function that prints a square with the character #

    Args:
        size: size of the square printed

    Returns:
        No return

    Raises:
        TypeError: If size is not an integer number


    """
    # check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # check if size is a non-integer negative
    if size < 0:
        raise ValueError("size must be >= 0")
    # print the square with the character #

    for count in range(size):
        print("#" * size)
