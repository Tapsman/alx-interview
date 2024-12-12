#!/usr/bin/python3
"""
Finds the prime numbers
"""


def primeNumbers(n):
    """
    This function will output numbers of 1 and n
    Return: The function will return (Ben or Maria)
    as either winner, if not found, NONE
    """

    primeNums = []
    filt = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filt[prime]):
            primeNums.append(prime)
            for i in range(prime, n + 1, prime):
                filt[i] = False
    return primeNums


# Now function checkes for winner
def isWinner(x, nums):
    """
    The function will then find the winner
    Args:
        x: The number of the rounds
        nums: Limit of the top at each of the rounds
    Return:
        winner of which is (Ben or Maria) or NONE if
        winner is not found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNums = primeNumbers(nums[i])
        if len(primeNums) % 2 == 0:
            Ben = Ben + 1
        else:
            Maria = Maria + 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
