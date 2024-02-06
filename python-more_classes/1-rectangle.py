#!/usr/bin/python3
class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        if type(width) is not int or type(height) is not int or width < 0 or height < 0:
            raise ValueError("width and height must be non-negative integers")

        self.__width, self.__height = width, height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int or value < 0:
            raise ValueError("width must be a non-negative integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int or value < 0:
            raise ValueError("height must be a non-negative integer")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2
