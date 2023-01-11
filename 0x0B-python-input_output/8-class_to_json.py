#!/usr/bin/python3
"""Defines a function that returns a dictionary desc."""


def class_to_json(obj):
    """Returns a dictionary description.

    Args:
        obj (obj): The object to convert
    Return:
        Dictionary description
    """
    return obj.__dict__
