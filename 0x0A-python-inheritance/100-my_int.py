#!/usr/bin/python3
"""Defines a class MyInt that inherits from Int."""


class MyInt(int):
    """Represents an integer."""

    def __eq__(self, value):
        """Change behavior of == with !=."""
        return self.real != value

    def __ne__(self, value):
        """Change behavior of != with ==."""
        return self.real == value
