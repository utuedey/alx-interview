#!/usr/bin/python3
"""
Module for creating a pascal triangle
"""


def pascal_triangle(n):
    """Returns a list of lists of integers
       Representing the pascal's triangle of n.
    """
    triangle = []

    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif j > 0 or j > i:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
