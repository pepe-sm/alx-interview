#!/usr/bin/python3
"""The minimum operations"""


def minOperations(n):
    """Computes the fewest number of operations needed to result in exactly n H"""
    if not isinstance(n, int):
        return 0
    _count = 0
    board = 0
    done = 1
    while done < n:
        if board == 0:
            board = done
            done += board
            _count += 2
        elif n - done > 0 and (n - done) % done == 0:
            board = done
            done += board
            _count += 2
        elif board > 0:
            done += board
            _count += 1
    return _count
