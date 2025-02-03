#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
Class Shape
"""


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
        self.__radius = radius

    def area(self):
        """
        area method
        """
        return 3.14159265359 * self.__radius ** 2

    def perimeter(self):
        """
        perimeter method
        """
        return 2 * 3.14159265359 * self.__radius


class Rectangle(Shape):
    """
    Class Rectangle
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.
        """
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
    if not isinstance(shape, Shape):
        raise TypeError("shape is not an instance of Shape")
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
