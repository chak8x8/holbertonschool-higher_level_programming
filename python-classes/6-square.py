#!/usr/bin/python3
"""Defines a square with size and position attributes."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position.

        Args:
            size (int): The size of the square.
            position (tuple): The (x, y) position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using `#`, considering position."""
        if self.__size == 0:
            print("")
            return

        # Print vertical spacing (position[1])
        for _ in range(self.__position[1]):
            print("")

        # Print square with horizontal spacing (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
