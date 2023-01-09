#!/usr/bin/python3
"""Defines a function that checks if a object is related to a class."""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance or a subclass of a_class.

    Args:
        obj (any): The object passed
        a_class (type): The class to be checked
    Returns:
        True if obj is an instance of the class
        False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
