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
        if not isinstance(value, int):
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


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self._Rectangle__width = size
        self._Rectangle__height = size

    def area(self):
        """ Method that returns the area of the square """
        return self.__size * self.__size

    def __str__(self):
        """ Method that returns the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
