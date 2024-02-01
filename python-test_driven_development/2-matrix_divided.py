#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.

The function matrix_divided divides each element of a matrix by a number.
It checks for the correct data types and sizes of the input matrix and the
divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists of ints/floats): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of list of floats: A new matrix with each element of the input
                matrix divided by the divisor, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix contains non-numbers, contains rows of
                different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")

    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or div != div:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
