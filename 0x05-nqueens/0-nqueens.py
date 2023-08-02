#!/usr/bin/python3
"""
0-nqueens module
A program that solves the N queens problem.
"""
import sys

# List of possible solutions to the N queens problem
solutions = []


board_size = 0

# possible positions on the chessboard
positions = None


def get_input():
    """Retrieve and validates the input argument
       Returns:
          size: the size of the chessboard
    """
    global board_size
    board_size = 0
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(arguments[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def is_attacking(pos_0, pos_1):
    """checks if the positions of two queens are in an attacking mode
       Args:
         pos_0 (list or tuple): The first queen's position.
         pos_1 (list or tuple): The second queen's position.
       Returns:
         bool: True if the queens are in an attacking position else False.
    """
    if (pos_0[0] == pos_1[0]) or (pos_0[1] == pos_1[1]):
        return True
    return abs(pos_0[0] - pos_1[0]) == abs(pos_0[1] - pos_1[1])


def group_exists(group):
    """Checks if a group exists in the list of solutions.
       Args:
          group (list of integers): A group of possible positions.
       Returns:
          bool: True if it exists, otherwise False.
    """
    global solutions
    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == board_size:
            return True
    return False


def nqueens_solver(row, group):
    """solution for the n queens problem.
       Args:
         row (int): The current row in the chessboard.
         group (list of lists of integers): The group of valid positions.
    """
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([position[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(position[a].copy())
            if not any(used_positions):
                nqueens_solver(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Gets the solutions for the given chessboard size. """
    global position, n
    position = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    nqueens_solver(a, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
