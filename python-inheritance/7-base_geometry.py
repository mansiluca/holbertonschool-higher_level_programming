#!/usr/bin/python3
"""
Module for testing the BaseGeometry class
"""


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
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
