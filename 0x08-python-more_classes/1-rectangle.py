#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Create a class Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the class Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter/setter method for the width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter/setter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
