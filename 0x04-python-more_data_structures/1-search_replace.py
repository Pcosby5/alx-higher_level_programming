#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through the elements in the input list
    for integer in my_list:
        # Check if the current element is equal to the 'search' element
        if integer == search:
            # If it matches, append the 'replace' element to the new list
            new_list.append(replace)
        else:
            # If it doesn't match, keep the current element as is
            new_list.append(integer)

    return new_list
