#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """
    Rectangle class that defines a rectangle with width and height.

    Attributes:
        number_of_instances (int): The number of Rectangle instances created.
        print_symbol (any): The symbol used
        for string representation of the rectangle.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a new Rectangle
            instance with optional width and height.

        width(self):
            Getter for the width attribute.

        width(self, value):
            Setter for the width attribute with validation.

        height(self):
            Getter for the height attribute.

        height(self, value):
            Setter for the height attribute with validation.

        area(self):
            Calculates and returns the area of the rectangle.

        perimeter(self):
            Calculates and returns the perimeter of the rectangle.

        __str__(self):
            Returns the string representation of the rectangle
            using the print_symbol.

        __repr__(self):
            Returns a string that can recreate the rectangle instance.

        __del__(self):
            Handles actions upon deletion of a rectangle instance.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.width for _ in range(self.height))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
