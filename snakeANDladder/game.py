from board import Board 
from player import Players as Player
from dice import Dice 

class Game:
    def __init__(self, players):
        self.board = Board()
        self.dice = Dice()
        self.players = [Player(player) for player in players]
        self.players_turn = 0

    def start(self):
        while not self._game_is_over():
            player = self.players[self.players_turn]
            roll_dice = self.dice.roll_dice()
            new_position = player.get_position() + roll_dice
            if new_position < self.board.get_board_size():
                player.set_position(new_position)
                print(f"{player.get_name()} rolled a dice and moved to new position {player.get_position()}")

            if new_position == self.board.get_board_size():
                print(f"{player.get_name()} won the game!!!")
                break

            self.players_turn = (self.players_turn+1) % len(self.players)

    
    def _game_is_over(self):
        for player in self.players:
            if player.get_position == self.board.get_board_size:
                return True
        return False


        