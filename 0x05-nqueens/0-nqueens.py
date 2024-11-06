#!/usr/bin/python3
"""
This is NQUEENS challenge
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    sol = []
    pos_queens = []
    # This is the coordinates of the queens format, row and column
    stop = False
    row = 0
    column = 0

    # And now to iterate throgh the row
    while row < n:
        goback = False

        # Now through the columns
        while column < n:
            # loop to check if the current column is indeed safe
            safe = True
            for cord in pos_queens:
                col = cord[1]
                if (col == column or col + (row-cord[0]) == column or
                        col - (row-cord[0]) == column):
                    safe = False
                    break

            if not safe:
                if column == n - 1:
                    goback = True
                    break
                column = column + 1
                continue
            #  Now toplace the queen
            cords = [row, column]
            pos_queens.append(cords)
            """
            If the last row appends the solution and will have to restart all
            to the not done row
            Provided that the last is safe in the row
            """
            if row == n - 1:
                sol.append(pos_queens[:])
                for cord in pos_queens:
                    if cord[1] < n - 1:
                        row = cord[0]
                        column = cord[1]
                for i in range(n - row):
                    pos_queens.pop()
                if row == n - 1 and column == n - 1:
                    pos_queens = []
                    stop = True
                row = row - 1
                column = column + 1
            else:
                column = 0
            break
        if stop:
            break
        """
         fail: It will have to go to the previous row
            and continues from the las safe coluumn incremented by one
        """
        if goback:
            row = row - 1
            while row >= 0:
                column = pos_queens[row][1] + 1
                """Deletes the preceded queen coordinates"""
                del pos_queens[row]
                if column < n:
                    break
                row = row - 1
            if row < 0:
                break
            continue
        row = row + 1

        for idx, val in enumerate(sol):
            if idx == len(sol):
                print(val, end='')
            else:
                print(val)
