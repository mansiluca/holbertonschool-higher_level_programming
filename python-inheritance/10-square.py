#!/usr/bin/python3
"""
Class BaseGeometry
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
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method that returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Method that returns the rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def print(self):
        """
        Method that prints the rectangle
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Method that returns the area of the square
        """
        return super().area()
