#!/usr/bin/python3
"""This is a 2D matrix"""

def rotate_2d_matrix(matrix):
    """
    This is a 2d matrix that rotates 90 degrees clockwise
    Saves left and right values top left and bottom
    Returns: Nothing
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            topLeft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i] # move top right th the bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topLeft # moves the top left to the top right
        right = right - 1
        left = left + 1
