#!/usr/bin/python3
"""
This is a function that is going to determine the fewest
number of coins needed to meet a given amount
"""


def makeChange(coins, total):
    """
    Will receive a coins and calculates how much change of
    th total will be needed
    """
    if total <= 0:
        return 0

    else:
        c = sorted(coins)
        c.reverse()
        count = 0
        for i in c:
            while(total >= i):
                count = count + 1
                total = total - i
        if total == 0:
            return count
        return -1
