#!/usr/bin/python3
"""
This module provides matrix_divided, a function that divides
every element of a matrix (a list of lists of numbers) by a number
and returns a new matrix with the results rounded to 2 decimals.
"""


def matrix_divided(matrix, div):
    """Divide all elements of matrix by div and return a new matrix.
    Each result is rounded to 2 decimal places; the input is not changed.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg)
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
