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

        # Determine whether it's AI's turn
        if is_ai_opponent and game.current_player == game.ai_symbol:
            print(f"AI ({difficulty} mode) is making its move...")
            row, col = game.execute_ai_move(difficulty)
            print(f"AI placed '{game.ai_symbol}' at row {row + 1}, column {col + 1}")
        else:
            try:
                user_input = input("Enter your move (row, col) or type 'undo': ").strip().lower()

                # Handle undo functionality
                if user_input == "undo":
                    undo_message = game.undo_last_move()
                    print(undo_message)
                    if undo_message == "Move undone.":
                        print(f"It's now {game.current_player}'s turn.")
                        game.display_board()  # Show updated board
                    continue

                # Handle player move input
                row, col = map(int, user_input.split(","))
                row, col = row - 1, col - 1  # Convert to 0-indexed

                if row not in range(3) or col not in range(3):
                    print("Invalid input. Please enter a number between 1 and 3.")
                    continue

                if game.make_move(row, col) != "Move successful":
                    print("Spot already taken. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter valid row and column numbers.")
                continue

        # Check for win or draw after every move
        if game.check_win():
            game.display_board()
            print(f"Player {game.current_player} wins!" if not is_ai_opponent else f"AI ({game.ai_symbol}) wins!")
            break
        elif game.check_draw():
            game.display_board()
            print("It's a draw! Well played!")
            break

        # Switch turns
        game.switch_player()


def restart_game():
    """
    Prompts the user to decide if they want to play again, exit, or view the final board.

    Returns:
        str: "restart" if the player wants to restart, "exit" to quit, or "view" to see the board.
    """
    while True:
        choice = input("Do you want to play again, exit, or view the final board? (restart/exit/view): ").lower()
        if choice in ["restart", "exit", "view"]:
            return choice
        print("Invalid input. Please enter 'restart', 'exit', or 'view'.")

if __name__ == "__main__":
    while True:
        # Prompt the player to choose a symbol
        player_symbol = choose_symbol()
        print(f"Player has chosen '{player_symbol}' as their symbol.")

        # Choose the game mode
        game_mode = input("Enter '1' to play against another player or '2' to play against the AI: ").strip()
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
