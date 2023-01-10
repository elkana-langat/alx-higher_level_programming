#!/usr/bin/python3
"""Defines a function that appends data to a file."""


def append_write(filename="", text=""):
    """Appends data to a file.

    Args:
        filename (str): The file to used
        text (any): The data to append
    Return:
        The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
