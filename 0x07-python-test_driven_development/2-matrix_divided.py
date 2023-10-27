#!/usr/bin/python3
"""

This module is composed by a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    # check if div is a number and not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # check if the input is a matrix(a list of lists)
    if not matrix or not isinstance(matrix, list):
        raise TypeError("Each row of the matrix must have the same size")

    # initialize the variable to store the length of the row
    length = 0

    for element in matrix:
        # check if all elements have the same size
        if not element or not isinstance(element, list):
            raise TypeError("Each row of the matrix must have the same size")

        if length != 0 and len(element) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for num in element:
            if not type(num) in (int, float):
                raise TypeError(
                    "Each row of the matrix must have the same size")

            length = len(element)

            # divide all elements of the matrix by div,rounded to 2dp
            result = list(
                map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
            return (result)
