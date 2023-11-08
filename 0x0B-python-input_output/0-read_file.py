#!/usr/bin/python3
"""
0-read_file
"""


def read_file(filename=""):
    """
    read_file - reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of file
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
