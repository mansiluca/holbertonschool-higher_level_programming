#!/usr/bin/python3
"""
Module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float).

    Returns:
        A new matrix with elements divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists
        of numbers or div is not a number.
        ZeroDivisionError: If div is zero.
        TypeError: If rows of the matrix are of inconsistent size.
        ValueError: If the matrix is empty.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("divisor must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not matrix or not all(matrix):
        raise ValueError("matrix cannot be empty")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    return [[round(elem / div, 2) for elem in row] for row in matrix]
