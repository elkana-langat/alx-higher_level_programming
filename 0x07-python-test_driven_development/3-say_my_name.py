#!/usr/bin/python3
"""
The module defines a function ``say_my_name(...)``.

It takes two arguments and adds them together and,
prints a string.

"""


def say_my_name(first_name, last_name=""):
    """Prints first and lastname passed.

    Args:
        first_name (str): The first String passed
        last_name (str): The second String passed
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
