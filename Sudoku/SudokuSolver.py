from typing import List


def checkGrid(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False

    return True


def solveGrid(grid):
    row = col = None
    # Find next empty cell
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if grid[row][col] == 0:
            for value in range(1, 10):
                if value not in grid[row]:
                    if value not in (
                            grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col],
                            grid[6][col],
                            grid[7][col], grid[8][col]):
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [grid[i][6:9] for i in range(6, 9)]
                        # Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if checkGrid(grid):
                                print("Grid Complete and Checked")
                                return True
                            else:
                                if solveGrid(grid):
                                    return True
            break
    grid[row][col] = 0


def sudoku_solver(grid: List[List[int]]) -> List[List[int]]:
    solveGrid(grid)
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
