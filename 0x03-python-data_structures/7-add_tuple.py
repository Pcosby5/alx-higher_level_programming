#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2elements
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    # Add first index of each tuple
    tuple_c = tuple_a[0] + tuple_b[0]
    # Add the second index of each tuple
    tuple_d = tuple_a[1] + tuple_b[1]
    return (tuple_c, tuple_d)

