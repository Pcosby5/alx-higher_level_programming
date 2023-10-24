#!/usr/bin/python3
"""
This module defines a Square class

It implements value and type checks for its attributes with area function
"""


class Square:
    """Square implementation
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retreives size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Checks size and sets it"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Implements area"""
        return (self.__size ** 2)

    def my_print(self):
        """Print an empty line"""
        if self.__size == 0:
            print('')
        else:
            """Print #"""
            for _ in range(self.__size):
                print("#" * self.__size)
