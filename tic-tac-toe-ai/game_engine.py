class GameEngine:
    """
    A class to represent the Tic-Tac-Toe game engine.

    This class manages the game board, player moves, win and draw conditions, and player switching.
    It provides methods to display the board, check game state, reset the game, and handle AI moves.
    """

    def __init__(self):
        """Initializes the game engine with an empty board and sets the current player to 'X'."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        """Displays the current state of the game board in a user-friendly format."""
        print("---------")
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("---------")

    def make_move(self, row, col):
        """
        Places the current player's symbol on the board at the specified row and column.

        Args:
            row (int): The row index for the move (0, 1, or 2).
            col (int): The column index for the move (0, 1, or 2).

        Returns:
            bool: True if the move is valid and placed successfully; False if the spot is already occupied.
        """
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

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
            if all([spot == self.current_player for spot in board[i]]) or \
               all([board[j][i] == self.current_player for j in range(3)]):
                return True
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] == self.current_player or \
           board[0][2] == board[1][1] == board[2][0] == self.current_player:
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

    def ai_move(self):
        """Placeholder for AI logic using Minimax Algorithm, to be implemented later."""
        pass  # AI logic will be added here in the future
