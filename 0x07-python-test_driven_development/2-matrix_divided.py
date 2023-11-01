#!/usr/bin/python3
"""

This module is composed by a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero


    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or not isinstance(matrix, list):
        raise TypeError("Each row of the matrix must have the same size")

    length = 0

    for element in matrix:
        if not element or not isinstance(element, list):
            raise TypeError("Each row of the matrix must have the same size")

        if length != 0 and len(element) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for num in element:
            if not type(num) in (int, float):
                raise TypeError(
                    "Each row of the matrix must have the same size")

            length = len(element)

            result = list(
                map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
            return (result)
