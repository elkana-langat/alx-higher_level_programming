#!/usr/bin/python3
"""
The module defines a base class ``Base``.

The ``Base`` is used to manage `id` attribute in all the
child classes and avoid duplicating code.

"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of a list_dictionary

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (any): it is a list of instance
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                obj_dict = []
                for i in list_objs:
                    obj_dict.append(i.to_dictionary())
                f.write(Base.to_json_string(obj_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json strin

        Args:
            json_string (str): JSON string representing a list of dict
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set

        Args:
            dictionary (dict): double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                a = cls(2, 2)
            else:
                a = cls(2)
            a.update(**dictionary)
            return a

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**i) for i in list_dict]
        except IOError:
            return []
