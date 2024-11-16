import random

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

    def display_board(self):
        """Displays the current state of the game board in a user-friendly format with clearer formatting."""
        print("\n   1   2   3")
        for idx, row in enumerate(self.board, 1):
            print(f"{idx}  " + " | ".join(row))
            if idx < 3:
                print("  ---|---|---")

    def make_move(self, row, col):
        """
        Attempts to place the current player's symbol on the board at the specified row and column.

        Args:
            row (int): The row index for the move (0, 1, or 2).
            col (int): The column index for the move (0, 1, or 2).

        Returns:
            str: Message indicating if the move was successful or if the spot is taken.
        """
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return "Move successful"
        return "Spot already taken"

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

    def get_available_moves(self):
        """
        Returns a list of available spots on the board.

        Returns:
            list of tuples: Each tuple contains the (row, col) coordinates of an empty spot.
        """
        return [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == " "]

    def ai_move(self):
        """Uses the Minimax algorithm to determine the best move for the AI."""
        best_score = -float('inf')
        best_move = None
        for (row, col) in self.get_available_moves():
            # Simulate AI move
            self.board[row][col] = self.ai_symbol
            score = self.minimax(0, False)  # Minimax call with depth=0 and minimizing for opponent
            # Undo move
            self.board[row][col] = " "
            if score > best_score:
                best_score = score
                best_move = (row, col)

        # Execute the best move
        if best_move:
            row, col = best_move
            self.board[row][col] = self.ai_symbol

    def minimax(self, depth, is_maximizing):
        """
        Minimax algorithm to find the optimal move for the AI, factoring in depth for faster wins or slower losses.
        Includes prioritization for blocking opponent's winning moves.
        """
        if self.check_win():
            return 10 - depth if self.current_player == self.ai_symbol else depth - 10
        elif self.check_draw():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for (row, col) in self.get_available_moves():
                self.board[row][col] = self.ai_symbol
                score = self.minimax(depth + 1, False)
                self.board[row][col] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for (row, col) in self.get_available_moves():
                self.board[row][col] = self.player_symbol
                if self.check_win():  # Detect potential player win
                    return -10  # Prioritize blocking
                score = self.minimax(depth + 1, True)
                self.board[row][col] = " "
                best_score = min(score, best_score)
            return best_score
