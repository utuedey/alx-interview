#!/usr/bin/env python3
"""
0-minoperations module - contains a method that
calculates the fewest number of operations(copy all & paste)
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """calculates the fewest number of operations needed
       to result in exactly n H characters in the file.
    """
    if not isinstance(n, int):
        return 0
    operation_counts = 0
    clipboard = 0
    completed = 1

    while completed < n:
        if clipboard == 0:
            # the first copy all and paste
            clipboard = completed
            completed += clipboard
            operation_counts += 2
        elif n - completed > 0 and (n - completed) % completed == 0:
            # copy all & paste
            clipboard = completed
            completed += clipboard
            operation_counts += 2
        elif clipboard > 0:
            # paste
            completed += clipboard
            operation_counts += 1
    return operation_counts
