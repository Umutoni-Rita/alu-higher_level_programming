#!/usr/bin/python3
"""This module defines MyList, a subclass of list with a sorted printer."""


class MyList(list):
    """A list subclass that can print its elements in ascending order."""

    def print_sorted(self):
        """Print the list sorted in ascending order.

        The list itself is not modified; a sorted copy is printed.
        """
        print(sorted(self))
