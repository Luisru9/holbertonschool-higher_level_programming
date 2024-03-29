#!/usr/bin/python3
"""This is a module containing a class for representing a Square."""


class Square:
    """A class representing a square.

    This class defines a square by its size.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
