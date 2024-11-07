#!/usr/bin/python3
""" Solves the N-Queens problem """

import sys


def solution(board, N):
    """ Prints the allocated ppositions to the queen """
    solution = []
    for i in range(N):
        for c in range(N):
            if c == board[i]:
                solution.append([i, c])
    print(solution)


def is_safe(board, i, row, col):
    """Checks if the position is safe for the queen"""
    return board[i] in (col, col - i + row, i - row + col)


def solve_n_queens(board, row, N):
    """Solves the N-Queens problem"""
    if row == N:
        # Print the solution
        solution(board, N)
    else:
        for col in range(N):
            allowed = True
            for i in range(row):
                if is_safe(board, i, row, col):
                    allowed = False
                    break
            if allowed:
                board[row] = col
                solve_n_queens(board, row + 1, N)


def chess_board(size):
    """Creates a chess board"""
    board = [0 * size for r in range(size)]
    return board


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    myboard = chess_board(N)
    solution = solve_n_queens(myboard, 0, N)
