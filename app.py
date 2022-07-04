import json
from http.client import HTTPException

from flask import Flask, render_template, request, jsonify
from sudoku import SudokuGenerator, SudokuSolver

app = Flask(__name__)

cur_game = None


@app.route("/", methods=["POST", "GET"])
def index():
    global cur_game
    if request.method == 'POST':
        level = request.form.get('level')
        sg = SudokuGenerator.SudokuGenerator(int(level))
        cur_game = sg.generateSudoku()
        return jsonify(cur_game)
    else:
        return render_template("index.html")


@app.route("/solvesudoku", methods=['GET'])
def solve_sudoku():
    global cur_game
    if cur_game:
        SudokuSolver.sudoku_solver(cur_game)
        return jsonify(cur_game)
    raise HTTPException(404, "No game found")


@app.route("/check-solution", methods=['POST'])
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
    app.run(debug=True)
