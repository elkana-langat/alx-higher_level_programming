#!/usr/bin/python3
"""Defines a function that write a string to a file."""


def write_file(filename="", text=""):
    """Write to a file.

    Args:
        filename (str): The name of the file to be written to
        text (any): The string to write
    Return:
        The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
