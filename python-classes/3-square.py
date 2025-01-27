#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
"""


class Square:
    """
    A class used to represent a square

    ...

    Attributes
    ----------
    size : int
        The size of a side of the square (default is 0)

    Methods
    -------
    area():
        Returns the area of the square
    """
    def __init__(self, size=0):
        """
        Parameters
        ----------
        size : int
            The size of a side of the square (default is 0)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the square

        Returns
        -------
        int
            The area of the square
        """
        return self.__size ** 2
