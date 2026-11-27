#!/usr/bin/python3
"""This module defines a Student class that can describe itself as a dict."""


class Student:
    """A class that represents a student by name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: The instance attributes, keyed by attribute name.
        """
        return self.__dict__
