#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of the Rectangle, validating it."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of the Rectangle, validating it."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
