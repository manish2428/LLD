from abc import ABC,abstractmethod
from player import Player
class Board(ABC):

    @abstractmethod
    def display_board():
        pass

class TicTacToe(Board):
    def __init__(self):
        self.board = [["_" for _ in range(3)] for _ in range(3)]

    #displayes the board
    def display_board(self):
        for row in self.board:
            print(" | ".join(row)) 
        print("\n")  
    
    #winner
    def check_win_status(self):
        # Check rows
        for row in self.board:
            if row[0] != "_" and row[0] == row[1] == row[2]:
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] != "_" and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return True

        # Check main diagonal
        if self.board[0][0] != "_" and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True

        # Check reverse diagonal
        if self.board[0][2] != "_" and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True

        return False

    #draw
    def is_board_full(self) -> bool:
        for row in self.board:
            if row[0] == '_' or row[1] == '_' or row[2] == '_':
                return False
        return True
    
    #check weather the particular index is empty or not
    def check_empty_index(self, row , col) -> bool:
        if self.board[row][col] == '_':
           return True
        return False

    def set_symbol(self, row, col, symbol):
        self.board[row][col] = symbol

    def game_status(self):
        if self.check_win_status():
            return "WIN"
        
        if self.is_board_full():
            return "DRAW"
        
        return "CONTINUE"


    