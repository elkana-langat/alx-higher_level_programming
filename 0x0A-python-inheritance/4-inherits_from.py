#!/usr/bin/python3
"""Defines a function that check if a object inherited from a class."""


def inherits_from(obj, a_class):
    """checks if an object is inherited from a class.

    Args:
        obj (any): The object to be checked
        a_class (type): The class to check
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
