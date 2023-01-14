#!/usr/bin/python3
"""
This module defines a function ``print_square(size)``

``print_square(...)`` prints a square with the character #

"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): The size of the square sides.

    Raise:
        TypeError: If size in not an integer
        ValueError: If the size is less than 0
        TypeError: If the size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if isinstance(size, int):
        if size < 0:
            raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
