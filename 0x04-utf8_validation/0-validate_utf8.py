#!/usr/bin/python3
"""
This is a task for the UTF-8 Validation
"""


def validUTF8(data):
    """
    The function will return a list of integers
    as its own data.
    Return: The function will then return True if the
    data is a valid UTF-8 encode otherwise False
    """

    num_byte = 0

    for i in data:
        if num_byte == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b11110:
                num_byte = 1
            elif i >> 4 == 0b11110:
                num_byte = 2
            elif i >> 3 == 0b111110:
                num_byte = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            num_byte = num_byte - 1
    return num_byte == 0
