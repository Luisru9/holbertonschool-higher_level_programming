#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Calculate area of the geometry.
        Raises:
            Exception: If area is not implemented.
        Args:
            self: the object itself.
        """
        raise Exception("area() is not implemented")
