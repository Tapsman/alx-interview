#!/usr/bin/python3
"""
Outputs and finds the Perimeter of an Island
"""


def island_perimeter(grid):
    """
    This is a function that will output, or
    find the perrimeter of an Island
    looping using i and j to find the Perimeter
    """
    per = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                per = per + 4
                if i > 0 and grid[i - 1][j] == 1:
                    per = per - 2
                if j > 0 and grid[i][j - 1] == 1:
                    per = per - 2
    return per
