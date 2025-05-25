# Dynamic-Sudoku-Generator-and-Solver

**Programming language**: Python

This project is to create an interactive Sudoku solver and generator for NxN puzzles. With Python and Tkinter as the GUI, the solver uses Backtracking, Constraint Propagation, and Branch and Bound algorithms to solve puzzles efficiently. Users can manually enter puzzles, create random puzzles, and visualize solving step-by-step. Optimizations for quick solving and uniqueness of puzzles are also included. Libraries such as NumPy are utilized for effective grid management.

---

📁 **File Structure**

```

sudoku_app/
│
├── main.py # Main GUI application file
├── sudoku_generator.py # Contains logic to generate Sudoku puzzles
├── sudoku_solver.py # Contains logic to solve Sudoku puzzles with visualization
├── README.md # Optional: Description and how to run the project

```
---
### File Descriptions

**main.py**
- Launches the GUI using tkinter.
- Displays a 9x9 Sudoku board using Entry widgets.
- Has buttons to Generate, Solve, Clear, and Pause/Resume.
- Handles coloring of cells (generated, user input, wrong answers).
- Communicates with the generator and solver modules.

**sudoku_generator.py**
- Builds a full valid Sudoku board.
- Randomly removes a number of cells to make a puzzle.
- Returns a puzzle board for the GUI to display.

**sudoku_solver.py**
- Reads the GUI entries into a 2D list.
- Solves the puzzle using backtracking.
- Updates GUI cells visually with each step.
- Highlights incorrect user entries in red.

---

### 🔄 Visual Steps

**Start** → **Main Menu** → **Generate/Solve/Exit**

**Generate Path**:
- Difficulty → Generate Grid → Remove Cells → Validate → Display

**Solve Path**:
- Input Puzzle → Validate → Solve → Display Result

**Exit** → End
