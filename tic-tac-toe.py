def display_board(board):
    """Displays the Tic-Tac-Toe board."""
    print("---------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("---------")

# Initialize the board with empty spaces
board = [[" " for _ in range(3)] for _ in range(3)]
display_board(board)
