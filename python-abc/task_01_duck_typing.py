#!/usr/bin/python3

"""
Duck typing - an object-oriented programming term used to refer to the application of
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Class Shape
    """
    @abstractmethod
    def area(self):
        """
        area method
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        perimeter method
        """
        pass


class Circle(Shape):
    """
    Class Circle
    """

    def __init__(self, radius):
        """
        Initializes a new Circle instance.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        area method
        """
        return 3.141592653589793 * self.__radius ** 2

    def perimeter(self):
        """
        perimeter method
        """
        return 2 * 3.141592653589793 * self.__radius


class Rectangle(Shape):
    """
    Class Rectangle
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.
        """
        if not isinstance(width, (int, float)) or width <= 0:
            raise TypeError("width must be a positive number")
        if not isinstance(height, (int, float)) or height <= 0:
            raise TypeError("height must be a positive number")

        self.__width = width
        self.__height = height

    def area(self):
        """
        area method
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        perimeter method
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    shape_info function
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
