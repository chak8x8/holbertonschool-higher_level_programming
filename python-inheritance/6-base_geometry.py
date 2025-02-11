#!/usr/bin/python3
"""Module defining the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Raises an exception indicating that
        the area method is not implemented."""
        raise Exception("area() is not implemented")
