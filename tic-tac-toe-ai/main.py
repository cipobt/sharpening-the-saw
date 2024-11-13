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
        # Display the current state of the board
        game.display_board()

        try:
            # Prompt player for their move (row and column)
            # Subtract 1 to convert user input (1-3) to zero-indexed format (0-2)
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1

            # Check if row and col are within the valid range (0 to 2)
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter a number between 1 and 3.")
                continue  # Go to the next iteration of the loop to prompt again

            # Attempt to make the move; if the spot is occupied, prompt again
            if game.make_move(row, col):
                # Check if the current move results in a win
                if game.check_win():
                    game.display_board()  # Show final board state
                    print(f"Player {game.current_player} wins!")  # Announce winner
                    break  # End game loop

                # Check if the game is a draw (no empty spaces left)
                elif game.check_draw():
                    game.display_board()  # Show final board state
                    print("It's a draw!")  # Announce draw
                    break  # End game loop

                # Switch to the other player if no win or draw
                game.switch_player()
            else:
                print("Spot already taken. Try again.")  # Inform player of invalid move

        except ValueError:
            print("Invalid input. Please enter a number.")


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
        # Prompt the player to choose a symbol, defaulting to 'X' if input is invalid
        player_symbol = choose_symbol()

        # Initialize the game engine with the chosen player symbol
        game = GameEngine()
        game.current_player = player_symbol

        # Start the main game loop
        play_game(game)

        # Ask the player if they want to restart the game
        if not restart_game():
            print("Thanks for playing!")  # Farewell message
            break  # Exit the game loop if the player does not want to restart
