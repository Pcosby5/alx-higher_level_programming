#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create empty sets to store elements present in only one of the sets
    unique_to_set_1 = set()
    unique_to_set_2 = set()

    # Iterate through the elements in set_1
    for item in set_1:
        # Check if the item is not in set_2
        if item not in set_2:
            # If it's only in set_1, add it to unique_to_set_1
            unique_to_set_1.add(item)

    # Iterate through the elements in set_2
    for item in set_2:
        # Check if the item is not in set_1
        if item not in set_1:
            # If it's only in set_2, add it to unique_to_set_2
            unique_to_set_2.add(item)

    # Combine the elements that are unique to each set
    only_diff_elements_set = unique_to_set_1.union(unique_to_set_2)

    return only_diff_elements_set
