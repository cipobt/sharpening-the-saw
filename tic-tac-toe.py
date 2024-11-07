def display_board(board):
    """Displays the Tic-Tac-Toe board."""
    print("---------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("---------")


def player_move(board, player):
    """Handles a player's move."""
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column (1-3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That spot is already taken. Try again.")
        except (IndexError, ValueError):
            print("Invalid input. Please enter numbers between 1 and 3.")


# Initialize the board with empty spaces
board = [[" " for _ in range(3)] for _ in range(3)]
display_board(board)

