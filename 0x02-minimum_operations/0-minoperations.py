#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    This is a function that can execute only two operations
    Then copy's all and pastes them
    """
    if n <= 1:
        return 0

    operands = 0
    div = 2

    while n > 1:
        while n % div == 0:
            operands = operands + div
            n //= div
        div = div + 1

    return operands
