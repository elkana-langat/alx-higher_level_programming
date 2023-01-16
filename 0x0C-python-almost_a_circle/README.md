# 0x0C. Python - Almost a circle

## Background COntext
The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:
	. Import
	. Exceptions
	. Class
	. Private attribute
	. Getter/Setter
	. Class method
	. Static method
	. Inheritance
	. Unittest
	. Read/Write file

You will also learn about:
	. args and kwargs
	. Serialization/Deserialization
	. JSON

## 0. If it's not testes it doesn't work
All your files, classes and methods must be unit tested and be PEP 8
validated.

## 1. Base class
Write the first class Base:
CReate a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package.
Create a file named models/base.py:
	. Class Base:
		. private class attribute __nb_objects = 0
		. class constructor: def __init__(self, id=None):
This class will be the "base" of all other classes in this project. The goal of it is to manage id attribute in all your future classes and avoid duplicating the same code.

## 2. First Rectangle

