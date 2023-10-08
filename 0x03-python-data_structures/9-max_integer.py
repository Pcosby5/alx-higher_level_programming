#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    # Initialize max value with first element in my_list
    max_int = my_list[0]
    # Iterate through the list starting from 2nd element
    for current_element in my_list[1:]:
        # compare current element with max value
        if current_element > max_int:
            max_int = current_element
    return max_int
