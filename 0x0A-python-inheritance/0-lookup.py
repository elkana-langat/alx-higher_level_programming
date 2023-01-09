#!/usr/bin/python3
"""Defines an function that looks up attributes of an object."""


def lookup(obj):
    """Returns the list of available attribues and methods of an object.
    Args:
        obj (obj): The object passed
    """
    return dir(obj)
