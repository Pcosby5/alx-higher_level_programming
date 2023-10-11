#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix of the same size as the input matrix
    new_matrix = []

    # Iterate through the rows of the input matrix
    for row in matrix:
        # Create a list to store the squared values for the current row
        row_squared = []

        # Iterate through the elements of the current row and compute their squares
        for column in row:
            squared_column = column ** 2
            row_squared.append(squared_column)

        # Append the squared row to the new matrix
        new_matrix.append(row_squared)

    return new_matrix
