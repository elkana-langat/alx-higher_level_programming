#!/usr/bin/python3
"""Defines a function that returns JSON rep of an object."""
import json


def to_json_string(my_obj):
    """Returns JSON rep of an object.

    Args:
        my_obj (obj): The object to be converted
    Return:
        JSON rep
    """
    return json.dumps(my_obj)
