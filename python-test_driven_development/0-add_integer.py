#!/usr/bin/python3
"""
This module defines the add_integer function.
"""
import math

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, defaults to 98.

    Raises:
        TypeError: If a or b is neither int nor float, or if a or b is inf/NaN.

    Returns:
        int: The sum of a and b, cast to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for inf or NaN explicitly:
    if isinstance(a, float) and (math.isinf(a) or math.isnan(a)):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (math.isinf(b) or math.isnan(b)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
