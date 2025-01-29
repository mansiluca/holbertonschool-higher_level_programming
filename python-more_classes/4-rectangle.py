#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """
    Rectangle class that defines a rectangle
    by its width and height.

    Attributes:
        width (int): The width of the rectangle.
        Must be a non-negative integer.
        height (int): The height of the rectangle.
        Must be a non-negative integer.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a new Rectangle
            instance with the specified width
            and height.

        width(self):
            Retrieves the width of the rectangle.

        width(self, value):
            Sets the width of the rectangle.
            Ensures the value is a non-negative integer.

        height(self):
            Retrieves the height of the rectangle.

        height(self, value):
            Sets the height of the rectangle.
            Ensures the value is a non-negative integer.

        area(self):
            Calculates and returns the
            area of the rectangle.

        perimeter(self):
            Calculates and returns the
            perimeter of the rectangle.
            Returns 0 if either width
            or height is 0.

        __str__(self):
            Returns a string representation of the
            rectangle using '#' characters.

        __repr__(self):
            Returns an official string representation
            of the Rectangle instance.
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

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
