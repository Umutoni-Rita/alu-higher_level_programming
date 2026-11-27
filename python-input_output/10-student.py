#!/usr/bin/python3
"""This module defines a Student class with a filtered dict representation.
"""


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

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to keep. If it
                is a list of strings, only those attributes are returned;
                otherwise all attributes are returned.

        Returns:
            dict: The selected instance attributes, keyed by name.
        """
        if (isinstance(attrs, list) and
                all(isinstance(name, str) for name in attrs)):
            return {name: self.__dict__[name] for name in attrs
                    if name in self.__dict__}
        return self.__dict__
