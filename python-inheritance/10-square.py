#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square using Rectangle."""

    def __init__(self, size):
        """Initializes a square with size validation."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Call Rectangle constructor

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size
