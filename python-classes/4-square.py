#!/usr/bin/python3
"""Defines a Square class with a private size attribute, getter, and setter."""

class Square:
    """Represents a square with size validation and an area method."""

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size  # Uses the setter to validate size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the square's area."""
        return self.__size * self.__size
