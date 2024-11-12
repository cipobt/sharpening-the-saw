from game_engine import GameEngine
from utils import choose_symbol

def play_game(game):
    """
    Runs the main game loop, allowing players to take turns and checking for win or draw conditions.

    Args:
        game (GameEngine): An instance of the GameEngine class to manage the game state.

    The function continuously prompts the player to enter row and column values to make a move.
    It checks for a win or draw after each move, switching players if the game is not over.
    """
    while True:
        game.display_board()
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
        if game.make_move(row, col):
            if game.check_win():
                game.display_board()
                print(f"Player {game.current_player} wins!")
                break
            elif game.check_draw():
                game.display_board()
                print("It's a draw!")
                break
            game.switch_player()
        else:
            print("Spot already taken. Try again.")

def restart_game():
    """
    Prompts the user to decide if they want to play again.

    Returns:
        bool: True if the player chooses to restart the game, False otherwise.
    """
    choice = input("Do you want to play again? (y/n): ").lower()
    return choice == "y"

if __name__ == "__main__":
    """
    Main entry point for the game. Sets up the game loop, allows players to choose their symbols,
    and initiates the game, providing the option to restart after each game.
    """
    while True:
        player_symbol = choose_symbol()
        game = GameEngine()
        game.current_player = player_symbol
        play_game(game)

        # Prompt for restart
        if not restart_game():
            print("Thanks for playing!")
            break
