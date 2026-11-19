#!/usr/bin/python3
"""This module defines a function that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle of n rows as a list of lists of integers.

    Each row starts and ends with 1, and every inner number is the sum of
    the two numbers directly above it in the previous row.

    Args:
        n (int): The number of rows to build.

    Returns:
        list: A list of n rows (lists of ints), or [] if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(n - 1):
        prev = triangle[-1]
        row = [1]
        for i in range(1, len(prev)):
            row.append(prev[i - 1] + prev[i])
        row.append(1)
        triangle.append(row)
    return triangle
