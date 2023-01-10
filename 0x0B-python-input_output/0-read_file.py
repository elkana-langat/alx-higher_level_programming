#!/usr/bin/python3
"""Defines a function that reads a text file and prints it out."""


def read_file(filename=""):
    """Read file and print it out.

    Args:
        filename (str): The name of the file
    """
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
        for line in read_file:
            print(line, end="")
