#!/usr/bin/python3
"""
This module provides a function that prints a square with the character #.

The function print_square prints a square of a given size using the #
character. It checks for the correct data type and value of the size
argument.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0 or if size is a float and less than
                0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
