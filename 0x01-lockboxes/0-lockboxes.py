#!/usr/bin/python3
"""A function to check if lockboxes can be opened"""


def canUnlockAll(boxes):
    """
    The function receives a set of keys to add to box
    So a key with the same number of key will open the box
    Each box is numbered sequentially from 0 to n - 1 and each
    box may contain keys to the other boxes.
    """
    total_boxes = len(boxes)
    setofkey = [0]
    count = 0
    indx = 0

    while indx < len(setofkey):
        keyset = setofkey[indx]
        for k in boxes[keyset]:
            if 0 < k < total_boxes and k not in setofkey:
                setofkey.append(k)
                count = count + 1
        indx = indx + 1

    return count == total_boxes - 1
