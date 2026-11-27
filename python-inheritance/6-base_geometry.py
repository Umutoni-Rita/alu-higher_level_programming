#!/usr/bin/python3
"""This module defines a BaseGeometry class with an unimplemented area."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Compute the area of the shape (must be defined by subclasses).

        Raises:
            Exception: Always, because the base class has no area.
        """
        raise Exception("area() is not implemented")
