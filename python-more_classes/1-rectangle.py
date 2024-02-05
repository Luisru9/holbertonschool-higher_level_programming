#!/usr/bin/python3
class Rectangle:
    """Rectangle class with width and height attributes."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __str__(self):
        """String representation of the Rectangle."""
        return f"{{'_Rectangle__height': {self.__height}, '_Rectangle__width': {self.__width}}}"


# Create instances in the desired order
rectangle1 = Rectangle(width=2, height=4)
rectangle2 = Rectangle(width=10, height=3)

# Accessing the string representation of the instances
print(rectangle1)  # Output: {'_Rectangle__height': 4, '_Rectangle__width': 2}
print(rectangle2)  # Output: {'_Rectangle__height': 3, '_Rectangle__width': 10}
