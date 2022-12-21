#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Create a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter method for the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter method for the values passed."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                [print("#", end="") for k in range(self.__size)]
                print()
