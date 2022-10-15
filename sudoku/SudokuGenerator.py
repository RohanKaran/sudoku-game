from random import randint, shuffle
from .SudokuSolver import checkGrid


class SudokuGenerator:
    def __init__(self, attempts: int):
        self.sudoku = [[0] * 9 for _ in range(9)]
        self.attempts = attempts
        self.counter = 1

    def solveGrid(self, grid):
        # Find next empty cell
        row = col = None
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                for value in range(1, 10):
                    if not (value in grid[row]):
                        if value not in (
                            grid[0][col],
                            grid[1][col],
                            grid[2][col],
                            grid[3][col],
                            grid[4][col],
                            grid[5][col],
                            grid[6][col],
                            grid[7][col],
                            grid[8][col],
                        ):
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
                            if value not in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                if checkGrid(grid):
                                    self.counter += 1
                                    break
                                else:
                                    if self.solveGrid(grid):
                                        return True
                break
        grid[row][col] = 0

    # A backtracking/recursive function to check all possible combinations of numbers until a solution is found
    def fillGrid(self, grid):
        numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        row = col = None
        # Find next empty cell
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                shuffle(numberList)
                for value in numberList:
                    if not (value in grid[row]):
                        if value not in (
                            grid[0][col],
                            grid[1][col],
                            grid[2][col],
                            grid[3][col],
                            grid[4][col],
                            grid[5][col],
                            grid[6][col],
                            grid[7][col],
                            grid[8][col],
                        ):
                            # Identify which of the 9 squares we are working on
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
                            if not value in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                if checkGrid(grid):
                                    return True
                                else:
                                    if self.fillGrid(grid):
                                        return True
                break
        grid[row][col] = 0

    def generateSudoku(self):
        self.fillGrid(self.sudoku)
        while self.attempts > 0:
            # Select a random cell that is not already empty
            row = randint(0, 8)
            col = randint(0, 8)
            while self.sudoku[row][col] == 0:
                row = randint(0, 8)
                col = randint(0, 8)

            backup = self.sudoku[row][col]
            self.sudoku[row][col] = 0

            copyGrid = []
            for r in range(0, 9):
                copyGrid.append([])
                for c in range(0, 9):
                    copyGrid[r].append(self.sudoku[r][c])

            self.counter = 0
            self.solveGrid(copyGrid)
            if self.counter != 1:
                self.sudoku[row][col] = backup
                self.attempts -= 1

        return self.sudoku


#
# obj = SudokuGenerator(attempts=4)
# sudoku = obj.generateSudoku()
# print(sudoku)
