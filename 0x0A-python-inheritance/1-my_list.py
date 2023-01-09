#!/usr/bin/python3
"""Defines class MyList which inherits from list."""


class MyList(list):
    """Initailizes the MyList class."""
    def __init__(self):
        """Initializes the object."""
        list. __init__(self)

    def print_sorted(self):
        """Prints a sorted list."""
        print(sorted(self))
