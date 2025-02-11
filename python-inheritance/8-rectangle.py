#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""

from 7-base_geometry import BaseGeometry  # Ensure BaseGeometry is imported


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
