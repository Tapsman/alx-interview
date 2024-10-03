#!/usr/bin/python3
"""The pascals triangle"""


def pascal_triangle(n):
    """
    And now the function generates the triangle to nth row

    Args:
        int (n): which is the number of rows to be generated

    Returns: The Pascals triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for row_num in range(1, n):
        row = [1]
        for j in range(1, row_num):
            comp = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            row.append(comp)
        row.append(1)
        triangle.append(row)

    return triangle
