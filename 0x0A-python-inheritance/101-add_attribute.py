#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object.

    Args:
        obj (obj): The object to query
        name (str): The name of the attribute
        value (any): The value to be added
    Raises:
        TypeError: if new attribute can't be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
