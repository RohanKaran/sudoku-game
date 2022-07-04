from typing import List


def checkGrid(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False

    return True


def isSafe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def solveGrid(grid, row, col):
    # row = col = None
    # Find next empty cell
    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveGrid(grid, row, col + 1)
    for num in range(1, 10, 1):

        if isSafe(grid, row, col, num):

            # Assigning the num in
            # the current (row,col)
            # position of the grid
            # and assuming our assigned
            # num in the position
            # is correct
            grid[row][col] = num

            # Checking for next possibility with next
            # column
            if solveGrid(grid, row, col + 1):
                return True

        grid[row][col] = 0
    return False


def sudoku_solver(grid: List[List[int]]) -> List[List[int]]:
    solveGrid(grid, row=0, col=0)
    return grid


def valid_row(row, grid):
    temp = grid[row]
    # Removing 0's.
    temp = list(filter(lambda a: a != 0, temp))
    # Checking for invalid values.
    if any(0 > i > 9 for i in temp):
        print("Invalid value")
        return -1
    # Checking for repeated values.
    elif len(temp) != len(set(temp)):
        return 0
    else:
        return 1


def valid_col(col, grid):
    # Extracting the column.
    temp = [row[col] for row in grid]
    # Removing 0's.
    temp = list(filter(lambda a: a != 0, temp))
    # Checking for invalid values.
    if any(0 > i > 9 for i in temp):
        print("Invalid value")
        return -1
    # Checking for repeated values.
    elif len(temp) != len(set(temp)):
        return 0
    else:
        return 1


def valid_subsquares(grid):
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            temp = []
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    if grid[r][c] != 0:
                        temp.append(grid[r][c])
            # Checking for invalid values.
            if any(0 > i > 9 for i in temp):
                print("Invalid value")
                return -1
            # Checking for repeated values.
            elif len(temp) != len(set(temp)):
                return 0
    return 1


# Function to check if the board invalid.
def check_board(grid: List[List[int]]) -> bool:
    # Check each row and column.
    for i in range(9):
        res1 = valid_row(i, grid)
        res2 = valid_col(i, grid)
        # If a row or column is invalid then the board is invalid.
        if res1 < 1 or res2 < 1:
            return False
    # If the rows and columns are valid then check the sub squares.
    res3 = valid_subsquares(grid)
    if res3 < 1:
        return False
    else:
        return True
