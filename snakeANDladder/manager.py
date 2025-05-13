import threading
from game import Game

class GameManager:
    _instance = None
    _lock = threading.Lock()


    def __init__(self):
        self.games = []

    
    @staticmethod
    def get_instance():
        if not GameManager._instance:
            with GameManager._lock:
                if not GameManager._instance:
                    GameManager._instance = GameManager()
        return GameManager._instance
    
    def start_new_game(self, players_name):
        game = Game(players_name)
        self.games.append(game)
        threading.Thread(target=game.start).start()

        