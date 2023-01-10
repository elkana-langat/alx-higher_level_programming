#!/usr/bin/python3
"""Defines a function that writes an object to a file on JSON rep."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a textfile.

    Args:
        my_obj (obj): The object to be written
        filename (str): The name of the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
