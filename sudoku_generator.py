import random

# Sudoku banane wala class - ye humare puzzles generate karta hai
class SudokuGenerator:
    def __init__(self, difficulty="medium"):
        # 9x9 board initialize karo, shuru mein sab kuch zero rahega
        self.board =[[0] * 9 for _ in range(9) ]
        self.difficulty = difficulty  # kitna tough chahiyeh puzzle?
        
    def set_difficulty(self, difficulty):
        """Level set karo: easy, medium, hard"""
        self.difficulty = difficulty

    def is_safe(self, row, col, num):
        # Dekho ki number daalna safe hai ya nahi
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
       
        # Box check karo (3x3 grid)
        box_row, box_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False
        return True
       
    # Board ko random numbers se bharo
    def fill_board(self):
        for row in range(9):
            for col in range(9):
                # Agar cell khali hai to kuch daalo
                if self.board[row][col] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)  # Numbers ko mix karo
                    
                    for num in numbers:
                        if self.is_safe(row, col, num):
                            self.board[row][col] = num
                            if self.fill_board():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    # Kuch cells ko khaali kardo taaki puzzle ban sake
    def remove_cells(self):
        # Difficulty ke hisab se kitne cells remove karne hai
        difficulty_levels = {
            "easy": 35,    # Asaan - zyada cells bhare hue rahenge
            "medium": 45,  # Normal - balanced
            "hard": 55     # Mushkil - kam cells bhare hue rahenge
        }
        
        blanks = difficulty_levels.get(self.difficulty, 45)  # Default medium
        count = blanks
        while count > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1

    def generate(self):
        # Pehle poora board bharo fir cells remove karo
        self.fill_board()
        self.remove_cells()
        return self.board