import random

# function to generate 9x9 sudoku game
class SudokuGenerator:
    def __init__(self):
        self.board =[[0] * 9 for _ in range(9) ] # Initialize a 9x9 board with zeros

    def is_safe (self, row, col, num):
        for i in range(9):
            if self.board[row][i] ==num or self.board[i][col] ==num:
                return False
       
        box_row, box_col = row - row %3, col - col %3
        for i in range (3):
            for j in range(3):
                
                if self.board[box_row + i][box_col + j] == num:
                    return False
        return True
       
       #fill the board with random no
    def fill_board(self):
        for row in range(9):
            for col in range(9):
                
                if self.board[row][col] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    
                    for num in numbers:
                        if self.is_safe(row, col, num):
                            self.board[row][col] = num
                            if self.fill_board():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    #removes some digits to create puzzle
    def remove_cells(self, blanks=40):
        count =blanks
        while count >0:
            row =random.randint(0, 8)
            col = random.randint (0, 8)
            
            if self.board[row][col]  != 0:
                self.board[row][col]  =0
                count -=  1

    def generate(self):
        self.fill_board ()
        self.remove_cells ()
        return self.board
