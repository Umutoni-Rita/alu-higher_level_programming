#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""


class Square:
    """A class that represents a square by its size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The length of one side of the square (not validated).
        """
        self.__size = size
