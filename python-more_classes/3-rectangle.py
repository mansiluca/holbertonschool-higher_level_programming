#!/usr/bin/python3
"""
A module that defines a Rectangle class.
"""


class Rectangle:
    """
    A module that defines a Rectangle class.
    Classes:
        Rectangle:
            A class representing a rectangle, defined
            by its width and height.
            Methods:
                __init__(width=0, height=0):
                    Initializes a new Rectangle instance
                    with the specified width
                    and height.
                width:
                    Getter and setter for the rectangle's
                    width. Ensures width is
                    an integer and non-negative.
                height:
                    Getter and setter for the rectangle's
                    height. Ensures height is
                    an integer and non-negative.
                area():
                    Calculates the area of the rectangle
                    based on its width and
                    height.
                perimeter():
                    Calculates the perimeter of the
                    rectangle. Returns 0 if either
                    dimension is 0.
                __str__():
                    Provides a string representation of
                    the rectangle using the
                    '#' character. Returns an empty string
                    if width or height is 0.
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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))
