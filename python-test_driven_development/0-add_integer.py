#!/usr/bin/python3
"""
This module defines the add_integer function.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Raises:
        TypeError: If a or b is neither int nor float.

    Returns:
        int: The sum of a and b, casted to int.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
