#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """
    Rectangle class that defines a rectangle by its width and height.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): Symbol used for string representation of
        the rectangle.
    """

    """
    Initialize a new Rectangle instance.

    Args:
        width (int): Width of the rectangle. Defaults to 0.
        height (int): Height of the rectangle. Defaults to 0.
    """

    """
    Retrieve the width of the rectangle.

    Returns:
        int: The width of the rectangle.
    """

    """
    Set the width of the rectangle.

    Args:
        value (int): The width value to set.

    Raises:
        TypeError: If the width is not an integer.
        ValueError: If the width is negative.
    """

    """
    Retrieve the height of the rectangle.

    Returns:
        int: The height of the rectangle.
    """

    """
    Set the height of the rectangle.

    Args:
        value (int): The height value to set.

    Raises:
        TypeError: If the height is not an integer.
        ValueError: If the height is negative.
    """

    """
    Calculate the area of the rectangle.

    Returns:
        int: The area of the rectangle.
    """

    """
    Calculate the perimeter of the rectangle.

    Returns:
        int: The perimeter of the rectangle,
        or 0 if either width or height is 0.
    """

    """
    Return the string representation of the rectangle using the print_symbol.

    Returns:
        str: The string representation of the rectangle.
    """

    """
    Return the official string representation of the rectangle.

    Returns:
        str: A string that can recreate the rectangle instance.
    """

    """
    Delete the rectangle instance and decrement the number_of_instances.

    Prints:
        str: "Bye rectangle..." upon deletion.
    """

    """
    Determine which rectangle has a bigger or equal area.

    Args:
        rect_1 (Rectangle): The first rectangle.
        rect_2 (Rectangle): The second rectangle.

    Returns:
        Rectangle: The rectangle with the larger or equal area.

    Raises:
        TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
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

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
