#!/usr/bin/python3
"""
This module defines a Square class

It implements value and type checks for its attributes with area function
"""


class Square:
    """Square implementation
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Implements area"""
        return (self.__size ** 2)

    def my_print(self):
        """Print an empty line"""
        if self.__size == 0:
            print('')
        else:
            """Print the square with #"""
            for _ in range(self.__position[1]):
                print('')
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
