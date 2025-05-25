import tkinter as tk
from tkinter import messagebox
from sudoku_generator import SudokuGenerator
from sudoku_solver import SudokuSolver

class SudokuApp:
    def __init__( self, master):
        self.master = master
        self.master.title("Sudoku Generator & Solver")
        self.master.geometry("400x450")
        self.is_paused = False

        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.build_grid()
        self.build_buttons()

    def build_grid( self):
        for i in range(9):
            for j in range(9):
                
                bg = "light grey" if (i // 3 + j // 3) % 2 == 0 else "white"
                entry = tk.Entry(self.master, width=3, font=('Times New Roman', 18), justify='center', bg=bg)
                entry.grid(row=i, column=j, padx=1, pady=1, ipady=5)
                self.entries[i][j] = entry

    def build_buttons(self):
        frame = tk.Frame(self.master)
        frame.grid(row=9, column=0, columnspan=9, pady=10)

        tk.Button(frame, text="Generate", command=self.generate_puzzle).grid(row=0, column=0, padx=5)
        self.pause_btn = tk.Button(frame, text="Pause", command=self.toggle_pause)
        self.pause_btn.grid(row=0, column=1, padx=5)
        
        tk.Button(frame, text="Clear", command=self.clear_grid).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Solve", command=self.solve_puzzle).grid(row=0, column=3, padx=5)

    def generate_puzzle(self):
        self.generated_cells = set()
        generator = SudokuGenerator()
        puzzle = generator.generate()
        
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if puzzle[i][j] !=0:
                    self.entries[i][j].insert(0, str(puzzle[i][j]))
                    self.entries[i][j].config(fg='black', font=('Times New Roman', 18, 'bold'))
                    self.generated_cells.add((i, j))
                else:
                    self.entries[i][j].config(fg='blue', font=('Times New Roman', 18, 'normal'))

    def clear_grid(self):
        for i in range(9):
            for j in range(9):
               
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].config(fg='blue', font=('Times New Roman', 18, 'normal'))

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        self.pause_btn.config(text="Resume" if self.is_paused else "Pause")

    def pause_check(self):
        while self.is_paused:
            self.master.update()
            self.master.after(100)

    def solve_puzzle(self):
        solver = SudokuSolver(self.entries, self.master, pause_check=self.pause_check)
        solved_grid = solver.solve()

        if solved_grid is None:
            messagebox.showerror("No Solution", "Could not find a solution to the puzzle. ")
            return

        for i in range(9):
            for j in range(9):
                user_val =  self.entries[i][j].get()
                correct_val =str(solved_grid[i][j])

                self.entries[i][j].delete(0, tk.END )
                self.entries[i][j].insert(0, correct_val )

                if (i, j) in getattr(self, 'generated_cells', set()):
                    self.entries[i][j].config(fg='black', font=('Times New Roman', 18,'bold'))
                elif user_val != correct_val:
                    self.entries[i][j].config(fg='red',font=('Times New Roman ', 18, 'normal'))
                else:
                    self.entries[i][j].config(fg='blue',font=('Times New Roman', 18, 'normal'))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
