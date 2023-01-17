#!/usr/bin/python3
"""
The module defines a class ``Square``

``Square`` inherits from class ``Rectangle``

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes an instance of class Square

        Args:
            size (int): The size of the sides
            x (int): x
            y (int): y
            id (int): The id of the instance of the class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter and setter method of the size
        """
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return the string representation of a Square.
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
