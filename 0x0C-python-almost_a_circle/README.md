# 0x0C. Python - Almost a circle

## Background COntext
The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:
- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

You will also learn about:
- args and kwargs
- Serialization/Deserialization
- JSON

## 0. If it's not testes it doesn't work
All your files, classes and methods must be unit tested and be PEP 8
validated.

## 1. Base class
Write the first class Base:
CReate a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package.
Create a file named models/base.py:
- Class Base:
	- private class attribute __nb_objects = 0
	- class constructor: def __init__(self, id=None):
This class will be the "base" of all other classes in this project. The goal of it is to manage id attribute in all your future classes and avoid duplicating the same code.

## 2. First Rectangle
Write the class Rectangle that inherits from Base:

## 3. Validate attributes
Update the class Rectangle by addig validation of all setter methods and instantiation (id excluded):
- If the input is not an integer, raise the TyperError exception with the message "name of the attribute must be an integer.
- If the width or height is under or equal to 0, raise the ValueError exception.
- If x or y is under 0, raise the ValueError exception

## 4. Area first
Update the class Rectangle by adding the publuc method def are(self):
that returns the area value of the Rectangle instance

## 5. Display #0
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character #

## 6. "__str__"
Update the class Rectangle by overdiding the __str__ mthod so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

## 7. Display #1
Update the class Rectangle by improving the public method def display(self): to print to stdout the Rectangle instance with the character # by taking care of x and y

## 8. Update # 0
Update the class Rectangle by adding the public method def update(self, *args): that assigns an arguments to each attribute

## 9. Update#1
Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes

## 10. And now, the Square!
Write the class Square that inherits from Rectangle


