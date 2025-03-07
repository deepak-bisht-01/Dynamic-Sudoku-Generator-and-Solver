import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku generator & solver")
        self.root.geometry("400x450")

        # Create a 9x9 grid of Entry widgets
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()

        # Create buttons
        self.create_buttons()

    def create_grid(self):
        for i in range(9):
            for j in range(9):

                if (i // 3 + j // 3) % 2 == 0:
                    bg_color = "light blue"
                else:
                    bg_color = "light pink"

                # Create an Entry widget for each cell
                cell = tk.Entry(self.root, width=3, font=('Times new Roman', 18), justify='center', bg=bg_color)
                cell.grid(row=i, column=j, padx=1, pady=1, ipady=5)
                self.cells[i][j] = cell

    def create_buttons(self):
        # Frame to hold the buttons
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=9, column=0, columnspan=9, pady=10)


        generate_button = tk.Button(button_frame, text="Generate", command=self.generate)
        generate_button.grid(row=0, column=0, padx=5)


        pause_resume_button = tk.Button(button_frame, text="Pause/Resume", command=self.pause_resume)
        pause_resume_button.grid(row=0, column=1, padx=5)

 
        clear_button = tk.Button(button_frame, text="Clear", command=self.clear)
        clear_button.grid(row=0, column=2, padx=5)


        solve_button = tk.Button(button_frame, text="Solve", command=self.solve)
        solve_button.grid(row=0, column=3, padx=5)

    def generate(self):
        # Placeholder for generating a new Sudoku puzzle
        messagebox.showinfo("Generate", "Generate a new Sudoku puzzle")

    def pause_resume(self):
        # Placeholder for pause/resume functionality
        messagebox.showinfo("Pause/Resume", "Pause or Resume the game")

    def clear(self):
       
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)

    def solve(self):
        # Placeholder for solving the Sudoku puzzle
        messagebox.showinfo("Solve", "Solve the Sudoku puzzle")

if __name__ == "__main__":
    root = tk.Tk()
    sudoku_gui = SudokuGUI(root)
    root.mainloop()