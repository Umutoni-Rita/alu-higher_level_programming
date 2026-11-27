#!/usr/bin/python3
"""This module defines a Square class that can print itself with #."""


class Square:
    """A class that represents a square that can be printed to stdout."""

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

    def my_print(self):
        """Print the square to stdout using the # character.

        An empty line is printed if the size is 0.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
