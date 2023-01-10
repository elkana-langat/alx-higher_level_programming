#!/usr/bin/python3
"""Defines a function that creates aN object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (file): The name of the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data_obj = json.load(f)
