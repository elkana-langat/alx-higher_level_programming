#!/usr/bin/python3

def lookup(obj):
    """Returns the list of available attribues and methods of an object.
    Args:
        obj (obj): The object passed
    """
    return dir(obj)
