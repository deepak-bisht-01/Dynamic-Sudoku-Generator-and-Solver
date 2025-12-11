import tkinter as tk
from tkinter import messagebox
from sudoku_generator import SudokuGenerator
from sudoku_solver import SudokuSolver

class SudokuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Generator & Solver")
        self.master.geometry("450x500")
        self.is_paused = False
        self.difficulty = "medium"  # Default level

        # 9x9 grid ke liye entries banaye
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.build_grid()
        self.build_buttons()

    def validate_input(self, char):
        """Sirf 0-9 tak ke numbers allow karo"""
        # Khali input allow karo
        if char == "":
            return True
        # Sirf ek digit 0-9 tak hi lenge
        if len(char) == 1 and char.isdigit():
            num = int(char)
            return 0 <= num <= 9
        # Baaki sab reject
        return False

    def on_invalid_input(self):
        """Agar galat input ho to kya karna hai"""
        pass

    def build_grid(self):
        # Input validation register karo
        vcmd = (self.master.register(self.validate_input), '%P')
        invcmd = (self.master.register(self.on_invalid_input),)
        
        for i in range(9):
            for j in range(9):
                # Alternate colors for boxes
                bg = "light grey" if (i // 3 + j // 3) % 2 == 0 else "white"
                entry = tk.Entry(self.master, width=3, font=('Times New Roman', 18), justify='center', bg=bg,
                               validate='key', validatecommand=vcmd, invalidcommand=invcmd)
                entry.grid(row=i, column=j, padx=1, pady=1, ipady=5)
                self.entries[i][j] = entry

    def build_buttons(self):
        # Difficulty level ke buttons ke liye frame
        difficulty_frame = tk.Frame(self.master)
        difficulty_frame.grid(row=9, column=0, columnspan=9, pady=5)
        
        tk.Label(difficulty_frame, text="Level:").grid(row=0, column=0, padx=5)
        self.difficulty_var = tk.StringVar(value="medium")
        
        # Radio buttons for difficulty levels
        tk.Radiobutton(difficulty_frame, text="Easy", variable=self.difficulty_var, 
                      value="easy", command=self.set_difficulty).grid(row=0, column=1, padx=5)
        tk.Radiobutton(difficulty_frame, text="Medium", variable=self.difficulty_var, 
                      value="medium", command=self.set_difficulty).grid(row=0, column=2, padx=5)
        tk.Radiobutton(difficulty_frame, text="Hard", variable=self.difficulty_var, 
                      value="hard", command=self.set_difficulty).grid(row=0, column=3, padx=5)

        # Main action buttons ke liye frame
        frame = tk.Frame(self.master)
        frame.grid(row=10, column=0, columnspan=9, pady=5)

        tk.Button(frame, text="Generate", command=self.generate_puzzle).grid(row=0, column=0, padx=5)
        self.pause_btn = tk.Button(frame, text="Pause", command=self.toggle_pause)
        self.pause_btn.grid(row=0, column=1, padx=5)
        
        tk.Button(frame, text="Clear", command=self.clear_grid).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Solve", command=self.solve_puzzle).grid(row=0, column=3, padx=5)

    def set_difficulty(self):
        """Difficulty level set karo"""
        self.difficulty = self.difficulty_var.get()

    def generate_puzzle(self):
        # Naya puzzle banaye
        self.generated_cells = set()
        generator = SudokuGenerator(self.difficulty)
        puzzle = generator.generate()
        
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if puzzle[i][j] != 0:
                    self.entries[i][j].insert(0, str(puzzle[i][j]))
                    self.entries[i][j].config(fg='black', font=('Times New Roman', 18, 'bold'))
                    self.generated_cells.add((i, j))
                else:
                    self.entries[i][j].config(fg='blue', font=('Times New Roman', 18, 'normal'))

    def clear_grid(self):
        # Sab kuch clear kardo
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].config(fg='blue', font=('Times New Roman', 18, 'normal'))

    def toggle_pause(self):
        # Pause/resume toggle karo
        self.is_paused = not self.is_paused
        self.pause_btn.config(text="Resume" if self.is_paused else "Pause")

    def pause_check(self):
        # Jab tak pause hai, wait karo
        while self.is_paused:
            self.master.update()
            self.master.after(100)

    def solve_puzzle(self):
        # Pehle check karo ki saare inputs valid hai ya nahi
        has_invalid = False
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                if val != "":
                    try:
                        num = int(val)
                        if not (0 <= num <= 9):
                            self.entries[i][j].config(fg='red', font=('Times New Roman', 18, 'bold'))
                            has_invalid = True
                    except ValueError:
                        self.entries[i][j].config(fg='red', font=('Times New Roman', 18, 'bold'))
                        has_invalid = True
        
        # Agar koi invalid input hai to warn karo
        if has_invalid:
            messagebox.showwarning("Galat Input", "Kuch cells mein galat numbers hai (0-9 ke beech ka hona chahiye). Ye laal dikh rahe hain.")
            return
        
        # Solver chalao with error handling
        try:
            solver = SudokuSolver(self.entries, self.master, pause_check=self.pause_check)
            solved_grid = solver.solve()

            if solved_grid is None:
                messagebox.showerror("Koi Solution Nahi", "Ye puzzle solve nahi ho sakta ya too complex hai.")
                return

            # Results dikhao
            for i in range(9):
                for j in range(9):
                    user_val = self.entries[i][j].get()
                    correct_val = str(solved_grid[i][j])

                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, correct_val)

                    if (i, j) in getattr(self, 'generated_cells', set()):
                        self.entries[i][j].config(fg='black', font=('Times New Roman', 18, 'bold'))
                    elif user_val != correct_val and user_val != "":
                        self.entries[i][j].config(fg='red', font=('Times New Roman', 18, 'bold'))
                    else:
                        self.entries[i][j].config(fg='blue', font=('Times New Roman', 18, 'normal'))
                        
        except Exception as e:
            # Koi bhi error aaye to user ko bataye
            messagebox.showerror("Error", f"Puzzle solve karte waqt error aaya: {str(e)}")
            return

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()