#!/usr/bin/python3
"""This module defines a Square class with a size getter and setter."""


class Square:
    """A class that represents a square with a controlled size property."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The length of one side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square.

        Returns:
            int: The length of one side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating it.

        Args:
            value (int): The new length of one side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of the square.

        Returns:
            int: The current area of the square (size squared).
        """
        return self.__size ** 2
