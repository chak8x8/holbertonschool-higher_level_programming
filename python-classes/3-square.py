#!/usr/bin/python3
"""Module that defines a Square class
with size validation and area calculation."""


class Square:
    """Defines a square with a private size attribute and an area method."""

    def __init__(self, size=0):
        """
        Initializes a square instance.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # Private attribute

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
