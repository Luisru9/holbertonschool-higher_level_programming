#!/usr/bin/python3
class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def __str__(self):
        return f"{{'_Rectangle__height': {self.__height}, '_Rectangle__width': {self.__width}}}"
