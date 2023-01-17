#!/usr/bin/python3
"""
This module defines a class ``Rectangle``.

Rectangle inherits from class ``Base.``

"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the object of rectangle.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): x
            y (int): y
            id (int): The id of the object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter and setter method of width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter and setter methods of height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle instance with the character #
        """
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for l in range(self.__width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """
        Assigns a key/value argument to be attributes
        """
        if args and len(args) != 0:
            i = 0
            for j in args:
                if i == 0:
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                if i == 1:
                    self.__width = j
                if i == 2:
                    self.__height = j
                if i == 3:
                    self.__x = j
                if i == 4:
                    self.__y = j
                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, l in kwargs.items():
                if k == "id":
                    if l is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = l
                if k == "width":
                    self.__width = l
                if k == "height":
                    self.__height = l
                if k == "x":
                    self.__x = l
                if k == "y":
                    self.__y = l

    def __str__(self):
        """
        Returns the string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
