#!/usr/bin/python3
import json


"""Defines a function that returns an object rep by a JSON string."""


def from_json_string(my_str):
    """Returns an Object from a JSON string.

    Args:
        my_str (any): The JSON string
    Return:
        A python object(data structure)
    """
    return json.loads(my_str)
