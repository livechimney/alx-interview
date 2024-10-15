#!/usr/bin/python3
"""
Minimum Operations calculates fewest number of ops
needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    Minimum Operations calculates fewest number of ops
    needed to result in exactly n H characters in the file
    """
    min = 2
    operations = 0
    while n > 1:
        while not n % min:
            operations += min
            n /= min
        min += 1
    return operations
