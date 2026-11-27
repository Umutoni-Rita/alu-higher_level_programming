#!/usr/bin/python3
"""This module defines a Square class with a size and a position."""


class Square:
    """A class that represents a square that has a size and a position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int): The length of one side of the square.
            position (tuple): Two positive integers (x, y) giving the
                horizontal and vertical offset used when printing.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the current position of the square.

        Returns:
            tuple: The (x, y) offset of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after validating it.

        Args:
            value (tuple): A tuple of 2 positive integers (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute the area of the square.

        Returns:
            int: The current area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square to stdout using # and the position offset.

        First position[1] empty lines are printed, then each row is
        shifted right by position[0] spaces. An empty line is printed
        if the size is 0.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
