#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Raises an exception indicating that
        the area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
