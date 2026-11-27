#!/usr/bin/python3
"""This module defines a Square class built on top of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square shape, which is a Rectangle with equal width and height."""

    def __init__(self, size):
        """Initialize a new Square with a validated size.

        Args:
            size (int): The length of each side, must be > 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Compute the area of the square.

        Returns:
            int: The size multiplied by itself.
        """
        return self.__size * self.__size
