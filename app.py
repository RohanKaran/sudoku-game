import json

from flask import Flask, jsonify, render_template, request

from sudoku import SudokuGenerator, SudokuSolver

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        level = request.form.get("level")
        sg = SudokuGenerator.SudokuGenerator(int(level))
        cur_game = sg.generateSudoku()
        return jsonify(cur_game)
    else:
        return render_template("index.html")


@app.route("/solvesudoku", methods=["POST"])
def solve_sudoku():
    grid = json.loads(request.form.get("grid"))
    return jsonify(SudokuSolver.sudoku_solver(grid))


@app.route("/check-solution", methods=["POST"])
def check_solution():
    grid = json.loads(request.form.get("grid"))
    if SudokuGenerator.checkGrid(grid):
        check = SudokuSolver.check_board(grid)
        if check:
            return {"res": "Correct!"}
        else:
            return {"res": "Wrong. Try again!"}
    else:
        return {"res": "Incomplete!"}


if __name__ == "__main__":
    app.run()
