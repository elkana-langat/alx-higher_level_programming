#!/usr/bin/python
"""Defines a function that adds a new attribute to an object."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object.

    Args:
        obj (obj): The object to query
        name (str): The name of the attribute
        value (any): The value to be added
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.name = getattr(obj, name, value)
