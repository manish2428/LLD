from manager import GameManager
class GameDemo:

    def run():
        game_manager = GameManager.get_instance()

        player1 = ["manish","mukesh","subham"]
        game_manager.start_new_game(player1)

        # player2 = ["player1","player2","player3","player4"]
        # game_manager.start_new_game(player2)

if __name__ == "__main__":
    GameDemo.run()