#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """
    This module defines the Rectangle class, which represents a 2D rectangle
    with integer width and height attributes. The class provides property
    setters to enforce that width and height are integers and are not set
    to negative values.

    Attributes:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is a negative value.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
