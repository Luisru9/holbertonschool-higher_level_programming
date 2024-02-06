#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        if not all(isinstance(val, int) and val >= 0 for val in (width, height)):
            raise ValueError("width and height must be non-negative integers")

        self.__width, self.__height = width, height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("width must be a non-negative integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("height must be a non-negative integer")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2
