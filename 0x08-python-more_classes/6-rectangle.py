#!/usr/bin/python3

"""Create a class Rectangle."""


class Rectangle:
    """Represents a Rectangle.

    Attributes:
        number_of_instances (int): Shows the number of instances the class has.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the data.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter and setter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter and setter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns a string representation of the rectangle.

        Prints # as it's outline.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append("#")
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns the official string representation of the rectangle."""
        rect = "Rectangle(" + str(self.__width) + ", "
        rect += str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Prints a string when the instance is deleted."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
