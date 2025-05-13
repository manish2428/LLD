from manager import GameManager
class GameDemo:

    def run():
        game_manager = GameManager.get_instance()

        player1 = ["manish","mukesh","subham"]
        game_manager.start_new_game(player1)

        player2 = ["test1","test2","test3","test4"]
        game_manager.start_new_game(player2)

if __name__ == "__main__":
    GameDemo.run()