#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
"""


class Square:
    """
    A class used to represent a square.

    ...

    Attributes
    ----------
    size : int
        The size of a side of the square (default is 0)

    Methods
    -------
    area():
        Returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Parameters
        ----------
        size : int, optional
            The size of a side of the square (default is 0)
        """
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns
        -------
        int
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters
        ----------
        value : int
            The size of a side of the square.

        Raises
        ------
        TypeError
            If `value` is not an integer.
        ValueError
            If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
