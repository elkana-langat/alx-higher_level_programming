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

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                if count == 1:
                    self.size = arg
                if count == 2:
                    self.x = arg
                if count == 3:
                    self.y = arg
                count += 1
        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.sizee, self.x, self.y)
                    else:
                        self.id = j
                if i == "size":
                    self.size = j
                if i == "x":
                    self.x == j
                if i == "y":
                    self.y = j

    def __str__(self):
        """
        Return the string representation of a Square.
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
