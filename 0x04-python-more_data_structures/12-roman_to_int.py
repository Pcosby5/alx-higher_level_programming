#!/usr/bin/python3

def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0

    # Create a dictionary to map Roman numerals to their integer values
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Create a list of integers by mapping each Roman numeral to its value
    numbers = [roman_dict[x] for x in roman_string] + [0]

    value_total = 0  # Initialize the total value

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            # Add the value if it's greater or equal to the next value
            value_total += numbers[i]
        else:
            # Subtract the value if it's less than the next value
            value_total -= numbers[i]

    return value_total  # Return the computed integer value for the Roman numeral
