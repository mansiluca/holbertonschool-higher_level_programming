#!/usr/bin/python3
""" Module that defines a class BaseGeometry """


class BaseGeometry:
    """
    Class BaseGeometry
    """

    def area(self):
        """
        Method that raises an Exception with the message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
