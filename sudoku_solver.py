import time
import tkinter as tk

class SudokuSolver:
    def __init__( self, entries,root, pause_check=None ):
        self.entries =entries
        self.root = root
        self.pause_check = pause_check or(lambda: None)
        self.grid = self.read_entries()

    def read_entries(self):
        grid = []
        for i in range(9):
            row = []
            
            for j in range(9):
                val = self.entries[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            grid.append(row)
        return grid

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
            
        box_row, box_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[box_row + i][box_col + j] == num:
                    return False
        return True

    def update_gui(self, row, col, num):
        self.pause_check ()
        self.entries[row][col].delete(0, tk.END )
        
        if num !=0:
            self.entries[row][col].insert(0, str(num) )
        self.entries[row][col].update()
        self.root.update ()
        time.sleep(0.05)

    def solve(self):
        
        if self._solve():
            return self.grid
        return None

    def _solve(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        
                        if self.is_valid(  row, col, num):
                            self.grid[row][col] =num
                            self.update_gui(row, col, num)
                            if self._solve():
                                return True
                            self.grid[row][col] =0
                            self.update_gui( row, col, 0)
                    return False
        return True
