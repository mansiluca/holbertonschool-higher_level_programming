#!/usr/bin/python3
"""
This module defines a class Square that initializes a square with a given size.
"""


class Square:
    """
    This class represents a square with a specific size.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            Must be an integer greater than or equal to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
