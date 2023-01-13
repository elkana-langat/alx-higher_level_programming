#!/usr/bin/python3
"""
Defines the function add_integer.

The function takes two integers and returns the sum,
of the integers.
"""


def add_integer(a, b=98):
    """Return the sum of two integers.

    Args:
        a (int, float): The first operand
        b (int, float): The second operanda

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
