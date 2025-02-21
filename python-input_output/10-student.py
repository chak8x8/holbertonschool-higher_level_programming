#!/usr/bin/python3
"""Defines a Student class with JSON serialization and attribute filtering."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If `attrs` is a list of strings, only those attributes are included.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the student.
        """
        json_dict = {}

        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            for attr in attrs:
                if isinstance(attr, str):  # Ensuring all attributes are strings
                    if hasattr(self, attr):  # Checking if attribute exists
                        json_dict[attr] = getattr(self, attr)  # Fetching attribute value
            return json_dict

        return self.__dict__  # Fallback if `attrs` is invalid
