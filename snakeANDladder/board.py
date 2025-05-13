from snake import Snake
from ladder import Ladder

class Board:
    BOARD_SIZE = 100
    def __init__(self):
        self.snakes = []
        self.ladders = []

    def _init_snake_and_ladder(self):

        #initializing snakes position
        self.snake.append(Snake(16,6))
        self.snake.append(Snake(48,26))
        self.snake.append(Snake(64,60))
        self.snake.append(Snake(93,73))
        

        #initializing ladder position
        self.ladder.append(Ladder(1,38))
        self.ladder.append(Ladder(4,14))
        self.ladder.append(Ladder(9,31))
        self.ladder.append(Ladder(21,42))
        self.ladder.append(Ladder(28,84))
        self.ladder.append(Ladder(51,67))
        self.ladder.append(Ladder(80,99))

    def get_board_size(self):
        return self.BOARD_SIZE
    
    def new_pos_after_snake_or_ladder(self, pos)->int:
        for snake in self.snakes:
            if snake.get_starting_index() == pos:
                return snake.get_end_index()
            
        for ladder in self.ladders:
            if ladder.get_starting_index() == pos:
                return ladder.get_end_index()
        
        return pos
    
        



