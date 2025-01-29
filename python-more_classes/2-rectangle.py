#!/usr/bin/python3
"""
Rectangle class defines the shape's width and height
and provides methods to compute its area and perimeter.
"""


class Rectangle:
    """
    Rectangle class definition.
    Classes:
        Rectangle:
            A class that represents a rectangle, defined by its width
            and height.
            Initialization:
                __init__(self, width=0, height=0):
                    Initialize a rectangle instance with optional width
                    and height.
                    Raises:
                        TypeError: If width or height is not an integer.
                        ValueError: If width or height is below 0.
            Properties:
                width (int):
                    Getter: Retrieve the current width of the rectangle.
                    Setter: Update the rectangle width. Must be a
                    non-negative integer.
                height (int):
                    Getter: Retrieve the current height of the rectangle.
                    Setter: Update the rectangle height. Must be a
                    non-negative integer.
            Methods:
                area(self):
                    Compute and return the rectangle's area (width * height).
                perimeter(self):
                    Compute and return the rectangle's perimeter
                    (2 * (width + height)).
                    Returns 0 if either width or height is 0.
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
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
