#!/usr/bin/python3
"""This module defines a BaseGeometry class with an integer validator."""


class BaseGeometry:
    """A base class for geometry shapes that can validate integers."""

    def area(self):
        """Compute the area of the shape (must be defined by subclasses).

        Raises:
            Exception: Always, because the base class has no area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a strictly positive integer.

        Args:
            name (str): The name of the value, used in error messages.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer (booleans are rejected).
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
