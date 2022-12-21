#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Create a Square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of a square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter method for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method for values passed.

        Args:
            value: The value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
