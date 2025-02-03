#!/usr/bin/python3
"""
Class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


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
        return self.__size ** 2
