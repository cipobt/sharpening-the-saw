from game_engine import GameEngine
from utils import choose_symbol

def play_game(game, is_ai_opponent):
    """
    Runs the main game loop, allowing players to take turns and checking for win or draw conditions.

    Args:
        game (GameEngine): An instance of the GameEngine class to manage the game state.
        is_ai_opponent (bool): True if the player is playing against the AI, False for two-player mode.

    The function continuously prompts the player to enter row and column values to make a move.
    It checks for a win or draw after each move, switching players if the game is not over.
    """
    while True:
        # Display the current state of the board
        game.display_board()

        # Check if it's the AI's turn in AI mode
        if is_ai_opponent and game.current_player == game.ai_symbol:
            print("AI is making its move...")
            game.ai_move()  # AI makes its move
            if game.check_win():
                game.display_board()
                print("AI wins!")
                break
            elif game.check_draw():
                game.display_board()
                print("It's a draw!")
                break
            game.switch_player()
            continue

        # Prompt player for their move (row and column)
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter a number between 1 and 3.")
                continue

            # Attempt to make the move; if the spot is occupied, prompt again
            if game.make_move(row, col):
                # Check for win condition
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
        # Prompt the player to choose a symbol
        player_symbol = choose_symbol()
        print(f"Player has chosen '{player_symbol}' as their symbol.")

        # Choose the game mode
        game_mode = input("Enter '1' to play against another player or '2' to play against the AI: ").strip()
        is_ai_opponent = game_mode == "2"

        # Initialize the game engine with the chosen player symbol
        game = GameEngine(player_symbol)
        game.current_player = player_symbol

        # Start the main game loop
        play_game(game, is_ai_opponent)

        # Prompt to restart the game
        if restart_game():
            game.reset_board()  # Reset the board for a new game
            print("Starting a new game!")
        else:
            print("Thanks for playing!")
            break
