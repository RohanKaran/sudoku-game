import json
from flask import Flask, render_template, request, jsonify
from Sudoku import SudokuGenerator, SudokuSolver

app = Flask(__name__)

global cur_game


@app.route("/", methods=["POST", "GET"])
def Index():
    global cur_game
    if request.method == 'POST':
        level = request.form.get('level')
        print(level)
        sg = SudokuGenerator.SudokuGenerator(int(level))
        cur_game = sg.generateSudoku()
        return jsonify(cur_game)
    else:
        return render_template("index.html")


@app.route("/solvesudoku", methods=['GET'])
def solve_sudoku():
    solution = SudokuSolver.sudoku_solver(cur_game)
    return jsonify(solution)


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