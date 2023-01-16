#!/usr/bin/python3
"""
The module defines a base class ``Base``.

The ``Base`` is used to manage `id` attribute in all the
child classes and avoid duplicating code.

"""


class Base:
    """
    Represents a class Base.

    Attributes:
        __nb_objects (int): The number of objects the class has.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the instance if class `Base`.

        Args:
            id (int): The id if the instance if the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
