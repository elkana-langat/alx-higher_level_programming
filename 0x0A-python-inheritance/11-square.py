#!/usr/bin/python3
"""Defines a class Square which inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square Object."""

    def __init__(self, size):
        """Initializes the Object.

        Args:
            size (int): The size of the Squares sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the string representation of a square."""
        return f"[Square] {self.__size}/{self.__size}"
