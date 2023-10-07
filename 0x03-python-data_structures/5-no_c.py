#!/usr/bin/python3
def no_c(my_string):
    # initialize empty string to store the new string
    new_string = ""
    for alpha in my_string:
        # check if alpha has no c or C
        if alpha != 'c' and alpha != 'C':
            # add alpha to new string
            new_string += alpha
    return new_string
