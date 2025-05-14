from board import TicTacToe
from player import Player

class Play:
    def __init__(self):
        self.board = TicTacToe()
        self.player1 = Player('Manish', 'X')
        self.player2 = Player('Mukesh', 'O')
        self.current_player = self.player1

    def start_game(self):
        while True:
            self.board.display_board()
            current_symbol = self.current_player.get_symbol()

            # Input validation for row and column
            # try:
            #     row = int(input("Enter the row number (0-2): "))
            #     col = int(input("Enter the column number (0-2): "))
            #     if row not in range(3) or col not in range(3):
            #         print("Invalid input. Please enter numbers between 0 and 2.")
            #         continue
            # except ValueError:
            #     print("Invalid input. Please enter valid integers.")
                # continue
            row,col = self._validate_user_input()

            # Check if the index is empty
            if self.board.check_empty_index(row, col):
                self.board.set_symbol(row, col, current_symbol)
                if self.board.game_status() == "WIN":
                    self.board.display_board()
                    print(f"{self.current_player.get_name()} won the match!!!")
                    break

                # Switch players
                self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            else:
                print("Index is already full. Please re-enter your move.")
                continue

            # Check if the board is full
            if self.board.game_status() == "DRAW":
                self.board.display_board()
                print("GAME DRAW !!")
                break
    
    def _validate_user_input(self):
        try:
            row = int(input("Enter row in range (0-2): "))
            col = int(input("Enter column in range (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid Input.Should be in range(0-2)")
                raise Exception("Invalid Input")
            return row,col
        
        except Exception as NumberError:
            print("Invalid input.")

if __name__ == '__main__':
    play_game = Play()
    play_game.start_game()