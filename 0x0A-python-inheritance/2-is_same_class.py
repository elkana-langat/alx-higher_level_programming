#!/usr/bin/python3
"""Defines a function that checks if an object is of specified class."""


def is_same_class(obj, a_class):
    """Checks if an object is of specified class.

    Args:
        obj (any): The object to be checked
        a_class (type): The class to check
    """
    if type(obj) == a_class:
        return True
    return False
