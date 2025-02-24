#!/usr/bin/python3
"""Generates Pascal's Triangle up to n rows."""

def pascal_triangle(n):
    """Returns a list of lists representing Pascal’s Triangle.

    Args:
        n (int): Number of rows.

    Returns:
        list: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []  # Return empty list for invalid input

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):  # Start from row index 1
        prev_row = triangle[i - 1]  # Get previous row
        new_row = [1]  # Every row starts with 1

        # Compute middle elements
        for j in range(1, len(prev_row)):  
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)  # Add the row to the triangle

    return triangle
