from game_engine import GameEngine
from utils import choose_symbol


def play_game(game, is_ai_opponent, difficulty):
    """
    Runs the main game loop, allowing players to take turns and checking for win or draw conditions.

    Args:
        game (GameEngine): An instance of the GameEngine class to manage the game state.
        is_ai_opponent (bool): True if the player is playing against the AI, False for two-player mode.
        difficulty (str): The difficulty level for AI ("Easy", "Medium", "Hard").
    """
    while True:
        game.display_board()

        # AI's move if enabled
        if is_ai_opponent and game.current_player == game.ai_symbol:
            print(f"AI ({difficulty} mode) is making its move...")
            row, col = game.execute_ai_move(difficulty)
            print(f"AI placed '{game.ai_symbol}' at row {row + 1}, column {col + 1}")
            if game.check_win():
                game.display_board()
                print(f"AI ({game.ai_symbol}) wins! Better luck next time!")
                break
            elif game.check_draw():
                game.display_board()
                print("It's a draw! Well played!")
                break
            game.switch_player()
            continue

        # Player's move
        try:
            print(f"Player {game.current_player}, it's your turn.")
            row = int(input("Enter row (1-3): ")) - 1
            if row not in range(3):
                print("Invalid input. Row must be between 1 and 3.")
                continue

            col = int(input("Enter column (1-3): ")) - 1
            if col not in range(3):
                print("Invalid input. Column must be between 1 and 3.")
                continue

            if game.make_move(row, col) == "Move successful":
                if game.check_win():
                    game.display_board()
                    print(f"Congratulations! Player {game.current_player} wins!")
                    break
                elif game.check_draw():
                    game.display_board()
                    print("It's a draw! Well played!")
                    break
                game.switch_player()
            else:
                print("Spot already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")


def restart_game():
    """
    Prompts the user to decide if they want to play again, exit, or view the final board.

    Returns:
        str: "restart" if the player wants to restart, "exit" to quit, or "view" to see the board.
    """
    while True:
        choice = input(
            "Do you want to play again, exit, or view the final board? (restart/exit/view): "
        ).lower()
        if choice in ["restart", "exit", "view"]:
            return choice
        print("Invalid input. Please enter 'restart', 'exit', or 'view'.")


if __name__ == "__main__":
    while True:

        # Prompt the player to choose a symbol
        player_symbol = choose_symbol()
        print(f"Player has chosen '{player_symbol}' as their symbol.")

        # Choose the game mode
        game_mode = input(
            "Enter '1' to play against another player or '2' to play against the AI: "
        ).strip()
        is_ai_opponent = game_mode == "2"

        # Choose difficulty if playing against AI
        difficulty = "Medium"
        if is_ai_opponent:
            difficulty = input("Choose AI difficulty (Easy, Medium, Hard): ").capitalize()
            if difficulty not in ["Easy", "Medium", "Hard"]:
                print("Invalid choice. Defaulting to Medium.")
                difficulty = "Medium"

        # Initialize the game engine
        game = GameEngine(player_symbol)
        game.current_player = player_symbol

        # Start the game
        play_game(game, is_ai_opponent, difficulty)

        # Handle restart or exit
        while True:
            choice = restart_game()
            if choice == "restart":
                game.reset_board()
                print("Starting a new game!")
                break
            elif choice == "exit":
                print("Thanks for playing! Goodbye!")
                exit(0)
            elif choice == "view":
                print("Final Board State:")
                game.display_board()
