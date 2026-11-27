#!/usr/bin/python3
"""This module defines a Rectangle class that can compare two rectangles."""


class Rectangle:
    """A class that represents a rectangle by its width and height.

    Attributes:
        number_of_instances (int): How many Rectangle instances exist.
        print_symbol (any): The symbol used to draw the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance and count it.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle.

        Returns:
            int: The current width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle after validating it.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle.

        Returns:
            int: The current height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle after validating it.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of the rectangle.

        Returns:
            int: The width multiplied by the height.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Compute the perimeter of the rectangle.

        Returns:
            int: Twice the sum of width and height, or 0 if either is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Build a printable picture of the rectangle using print_symbol.

        Returns:
            str: The rectangle drawn with print_symbol, or an empty
                string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        row = str(self.print_symbol) * self.__width
        return "\n".join(row for _ in range(self.__height))

    def __repr__(self):
        """Build a string that eval() can turn back into a Rectangle.

        Returns:
            str: A string of the form Rectangle(width, height).
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a goodbye message and uncount the deleted instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle.

        Returns:
            Rectangle: rect_1 if its area is bigger or equal, else rect_2.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
