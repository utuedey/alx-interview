#!/usr/bin/env python3
"""
0-rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    """Rotates a n X n matrix 90 degrees clockwise.
    """
    if not isinstance(matrix, list):
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    columns = len(matrix[0])
    if not all(map(lambda x: len(x) == columns, matrix)):
        return
    col, row = 0, rows - 1
    for i in range(columns * rows):
        if i % rows == 0:
            matrix.append([])
        if row == -1:
            row = rows - 1
            col += 1
        matrix[-1].append(matrix[row][col])
        if col == columns - 1 and row >= -1:
            matrix.pop(row)
        row -= 1
