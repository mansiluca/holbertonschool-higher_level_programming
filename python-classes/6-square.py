#!/usr/bin/python3
"""
This module defines a Square class that represents
a square with a specific size and position.
The Square class includes methods to calculate
the area of the square and to print the square
with the specified position.
"""


class Square:
    """
    A class used to represent a square

    Attributes
    ----------
    size : int
        The size of the square (default is 0)
    position : tuple
        The position of the square (default is (0, 0))

    Methods
    -------
    area():
        Returns the area of the square
    my_print():
        Prints the square with the specified position
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or not
                isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
