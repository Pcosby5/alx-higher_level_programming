#!/usr/bin/python3

"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""

def text_indentation(text):
    """
    Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string
    """

    # Check if the input 'text' is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Create a copy of the input text to avoid modifying the original
    format_text = text[:]

    # Iterate through the characters ".?:"
    for char in ".?:":
        # Split the string 'format_text' using the current character as the separator
        list_text = format_text.split(char)
        format_text = ""

        # Iterate through the resulting substrings
        for i in list_text:
            # Remove leading and trailing spaces from the substring
            i = i.strip(" ")

            # Append the substring followed by the separator to 'format_text'
            format_text = i + char if format_text is "" else format_text + "\n\n" + i + char

    # Print the formatted text with the last three characters (".?:" removed)
    print(format_text[:-3], end="")
