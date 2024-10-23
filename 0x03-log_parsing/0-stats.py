#!/usr/bin/python3

"""
This is a script that is going to read the std input
line after line
"""

import sys


def printRank(dic, size):
    """
    The function will then output the information
    """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


rankcode = {"200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0}


compute = 0
size = 0

try:
    for line in sys.stdin:
        if compute != 0 and compute % 10 == 0:
            printRank(rankcode, size)

        stlist = line.split()
        compute = compute + 1

        try:
            size = size + int(stlist[-1])
        except Exception:
            pass

        try:
            if stlist[-2] in rankcode:
                rankcode[stlist[-2]] += 1
        except Exception:
            pass
    printRank(rankcode, size)


except KeyboardInterrupt:
    printRank(rankcode, size)
    raise
