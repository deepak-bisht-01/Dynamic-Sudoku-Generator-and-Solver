# Dynamic Sudoku Generator and Solver

**Programming Language**: Python

This project is an interactive Sudoku application that allows users to generate random Sudoku puzzles, solve them manually, or watch the computer solve them step-by-step. Built with Python and Tkinter for the GUI, it provides an engaging way to play and learn Sudoku.

## 🎯 Key Features

- **Sudoku Generation**: Create random, solvable Sudoku puzzles with one click
- **Multiple Difficulty Levels**: Choose from Easy, Medium, or Hard difficulty settings
- **Interactive Solving**: Manually solve puzzles with real-time input validation (only 0-9 allowed)
- **Auto-Solving**: Watch the computer solve any puzzle using backtracking algorithm with visual feedback
- **Step-by-Step Visualization**: See how the solver works with the pause/resume feature
- **Input Validation**: Ensures only valid digits (0-9) can be entered in cells
- **Visual Feedback**: 
  - Generated numbers appear in bold black
  - User inputs appear in blue
  - Incorrect solutions are highlighted in red

## 📁 Project Structure

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
