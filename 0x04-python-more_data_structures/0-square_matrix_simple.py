#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [list(map(lambda func: func ** 2, k)) for k in matrix]
