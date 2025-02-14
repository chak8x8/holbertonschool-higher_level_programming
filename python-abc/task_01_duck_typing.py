#!/usr/bin/python3
"""Defines Shape abstract class and its implementations"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract class defining a blueprint for shapes"""

    @abstractmethod
    def area(self):
        """Calculates area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates perimeter of the shape"""
        pass


class Circle(Shape):
    """Concrete class representing a Circle"""

    def __init__(self, radius):
        if not isinstance(radius, (int, float)):  # Check type
            raise TypeError("Radius must be a number")
        self.__radius = abs(radius)

    def area(self):
        """Returns the area of the circle"""
        return math.pi * self.__radius ** 2

    def perimeter(self):
        """Returns the perimeter of the circle"""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Concrete class representing a Rectangle"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)  # FIXED


def shape_info(shape):
    """Prints area and perimeter of any shape (Duck Typing)"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
