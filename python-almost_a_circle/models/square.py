#!/usr/bin/python3
"""This module defines the Square class, which inherits from Rectangle.

A Square is a Rectangle whose width and height are always equal.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square shape: a Rectangle with the same width and height (size).

    All validation is inherited from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square using the Rectangle constructor.

        Args:
            size (int): length of each side, used as width and height.
            x (int): horizontal offset used by display, must be >= 0.
            y (int): vertical offset used by display, must be >= 0.
            id (int): identifier passed to the Base class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the square (its width and height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Set both width and height to value, using Rectangle validation."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign attributes from positional or keyword arguments.

        Positional order is id, size, x, y. Keyword arguments are
        ignored when at least one positional argument is given.
        """
        attributes = ("id", "size", "x", "y")
        if args:
            for name, value in zip(attributes, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in attributes:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
