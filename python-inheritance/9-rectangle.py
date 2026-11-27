#!/usr/bin/python3
"""This module defines a full Rectangle class built on top of BaseGeometry."""
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

    def area(self):
        """Compute the area of the rectangle.

        Returns:
            int: The width multiplied by the height.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description used by print() and str().

        Returns:
            str: The description in the form [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
