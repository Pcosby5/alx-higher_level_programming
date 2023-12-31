#!/usr/bin/python3
"""
This module defines a Square class

Its implements value and type checks for its attributes with area function
"""


class Square:
    """Square implementation
    """

    def __init__(self, size=0):
        self.size = size

    def __lt__(self, other):
        return self.__size < other.size

    def __le__(self, other):
        return self.__size <= other.size

    def __eq__(self, other):
        return self.__size == other.size

    def __ne__(self, other):
        return self.__size != other.size

    def __gt__(self, other):
        return self.__size > other.size

    def __ge__(self, other):
        return self.__size >= other.size

    @property
    def size(self):
        """Retreives the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size"""
        if not isinstance(size, (int, float)):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns the current size area"""
        return (self.__size ** 2)
