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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Method that returns the area of the square """
        return self.__size ** 2

    def __str__(self):
        """ Method that returns the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
