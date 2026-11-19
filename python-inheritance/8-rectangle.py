#!/usr/bin/python3
"""This module defines a Rectangle class built on top of BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle shape that is a subclass of BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle, must be > 0.
            height (int): The height of the rectangle, must be > 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
