#!/usr/bin/python3
"""Defines a class Rectangle which inherits BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the class.

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Find the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the object."""
        return f"[Rectangle] {self.__width}/{self.__height}"
