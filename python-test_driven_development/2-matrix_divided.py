#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): A matrix of integers/floats.
        div (int or float): The number to divide the elements by.

    Returns:
        list: A new matrix with each element divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # ✅ Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # ✅ Check if all elements inside matrix are integers or floats
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # ✅ Check if all rows have the same length
    row_length = len(matrix[0]) if matrix else 0  # Get the length of the first row
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # ✅ Check if div is an integer or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # ✅ Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # ✅ Divide each element in the matrix by div and round to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]
