#!/usr/bin/python3
"""This module defines the Rectangle class, which inherits from Base.

A Rectangle has a validated width, height and x/y position offset.
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle shape with width, height and an (x, y) position offset.

    Every attribute is private and validated through its property setter.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle and validate all of its attributes.

        Args:
            width (int): width of the rectangle, must be > 0.
            height (int): height of the rectangle, must be > 0.
            x (int): horizontal offset used by display, must be >= 0.
            y (int): vertical offset used by display, must be >= 0.
            id (int): identifier passed to the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def __validate(name, value, strictly_positive):
        """Raise an exception if value is not a valid integer for name.

        TypeError if it is not an int, ValueError if it is out of range.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if strictly_positive and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if not strictly_positive and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Get or set the width of the rectangle (an integer > 0)."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after checking that it is an integer > 0."""
        self.__validate("width", value, True)
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle (an integer > 0)."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after checking that it is an integer > 0."""
        self.__validate("height", value, True)
        self.__height = value

    @property
    def x(self):
        """Get or set the horizontal offset of the rectangle (int >= 0)."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x after checking that it is an integer >= 0."""
        self.__validate("x", value, False)
        self.__x = value

    @property
    def y(self):
        """Get or set the vertical offset of the rectangle (int >= 0)."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y after checking that it is an integer >= 0."""
        self.__validate("y", value, False)
        self.__y = value

    def area(self):
        """Return the area of the rectangle (width multiplied by height)."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with '#' characters, offset by x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign attributes from positional or keyword arguments.

        Positional order is id, width, height, x, y. Keyword arguments
        are ignored when at least one positional argument is given.
        """
        attributes = ("id", "width", "height", "x", "y")
        if args:
            for name, value in zip(attributes, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in attributes:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
