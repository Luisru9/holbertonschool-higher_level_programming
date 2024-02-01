#!/usr/bin/python3
class Square:
    """A class representing a square.

    This class defines a square by its size.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """Initialize a new Square instance with a given size.

        Args:
            size (int): The size of the square.

        Note:
            No type or value verification is performed on the size.
        """
        self.__size = size
