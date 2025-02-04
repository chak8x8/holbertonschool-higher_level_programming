#!/usr/bin/python3
"""Module that defines a Square class with size validation."""


class Square:
    """Defines a square with a private size attribute and size validation."""

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
