#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """Represents base geometry"""

    def area(self):
        """Not implimented raises an exception."""
        raise Exception("area() is not implimented")
