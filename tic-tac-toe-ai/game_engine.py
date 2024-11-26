from ai_logic import ai_move


class GameEngine:
    """
    A class to represent the Tic-Tac-Toe game engine.

    This class manages the game board, player moves, win and draw conditions, and player switching.
    It provides methods to display the board, check game state, reset the game, and handle AI moves.
    """

    def __init__(self, player_symbol="X"):
        """Initializes the game engine with an empty board and sets the current player to 'X'."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player_symbol = player_symbol
        self.ai_symbol = "O" if player_symbol == "X" else "X"
        self.current_player = self.player_symbol
        self.move_history = []

    def display_board(self):
        """Displays the current state of the game board in a user-friendly format
        with clearer formatting."""
        print("\n   1   2   3")
        for idx, row in enumerate(self.board, 1):
            print(f"{idx}  " + " | ".join(row))
            if idx < 3:
                print("  ---|---|---")

    def make_move(self, row, col):
        """
        Attempts to place the current player's symbol on the board at the specified row and column.
        Logs the move to the history if successful.
        """
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.move_history.append((row, col))  # Log the move
            return "Move successful"
        return "Spot already taken"

    def undo_last_move(self):
        """Undoes the last move made by removing it from the board and the move history."""
        if not self.move_history:
            return "No moves to undo."
        row, col = self.move_history.pop()
        self.board[row][col] = " "
        self.switch_player()  # Switch back to the player who made the move
        return "Move undone."

    def switch_player(self):
        """Switches the current player from 'X' to 'O' or from 'O' to 'X'."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        """
        Checks if the current player has won the game.

        Returns:
            bool: True if the current player has a winning combination; False otherwise.
        """
        board = self.board
        # Check rows and columns
        for i in range(3):
            if all([spot == self.current_player for spot in board[i]]) or all(
                [board[j][i] == self.current_player for j in range(3)]
            ):
                return True
        # Check diagonals
        if (
            board[0][0] == board[1][1] == board[2][2] == self.current_player
            or board[0][2] == board[1][1] == board[2][0] == self.current_player
        ):
            return True
        return False

    def check_draw(self):
        """
        Checks if the game has ended in a draw, meaning all cells are filled without a winner.

        Returns:
            bool: True if the board is full and no player has won; False otherwise.
        """
        return all(cell != " " for row in self.board for cell in row)

    def reset_board(self):
        """Resets the board to its initial empty state."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def execute_ai_move(self, difficulty):
        """
        Determines the AI's move using external AI logic and updates the board.

        Args:
            difficulty (str): The difficulty level ("Easy", "Medium", "Hard").

        Returns:
            tuple: The (row, col) position of the AI's move.
        """
        row, col = ai_move(self.board, self.ai_symbol, self.player_symbol, difficulty)
        self.board[row][col] = self.ai_symbol  # Place AI's symbol on the board
        return row, col
