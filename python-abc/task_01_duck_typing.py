#!/usr/bin/python3
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14159265359 * self.__radius ** 2

    def perimeter(self):
        return 2 * 3.14159265359 * self.__radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    if not isinstance(shape, Shape):
        raise TypeError("shape is not an instance of Shape")
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
