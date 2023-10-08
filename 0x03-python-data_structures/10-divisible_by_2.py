#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create an empty list to store the results
    results = []

    # Iterate through the elements in the input list
    for number in my_list:
        # Check if the current number is divisible by 2 (even)
        if number % 2 == 0:
            # If divisible by 2, append True to the results list
            results.append(True)
        else:
            # If not divisible by 2, append False to the results list
            results.append(False)

    # Return the list of True and False values
    return results
