#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each column in the current row
        for column in range(len(row)):
            # Print the integer value from the matrix with formatting
            print("{:d}".format(row[column]), end="")
            # Add a space if it's not the last column in the row
            if column < len(row) - 1:
                print(" ", end="")
        # Print a newline character to move to the next row
        print("")
