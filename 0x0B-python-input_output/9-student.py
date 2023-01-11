#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new object.

        Args:
            first_name (str): The firstname of the object
            last_name (str): The lastname of the object
            age (int): The age of the new object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary rep of the object."""
        return self.__dict__
