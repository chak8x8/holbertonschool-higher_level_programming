#!/usr/bin/python3
"""
This module defines the add_integer function.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, defaults to 98.

    Raises:
        TypeError: If a or b is neither int nor float,
                   or if a or b is inf/NaN.

    Returns:
        int: The sum of a and b, cast to an integer.
    """
    # 1) Verify a, b are int or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # 2) Check for inf or NaN explicitly via string comparison
    if isinstance(a, float):
        a_str = str(a).lower()  # e.g. 'inf', 'nan'
        if a_str in ('inf', '-inf', 'nan'):
            raise TypeError("a must be an integer")

    if isinstance(b, float):
        b_str = str(b).lower()
        if b_str in ('inf', '-inf', 'nan'):
            raise TypeError("b must be an integer")

    # 3) Return the integer sum
    return int(a) + int(b)
