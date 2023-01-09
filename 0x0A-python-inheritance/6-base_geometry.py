#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """Defines a method area which raises an exception."""

    def area(self):
        """Not implimented raises an exception."""
        raise Exception("area() is not implimented")
