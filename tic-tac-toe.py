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


def check_win(board, player):
    """Checks if a player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([spot == player for spot in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def check_draw(board):
    """Checks if the game is a draw."""
    return all(cell != " " for row in board for cell in row)


# Initialize the board with empty spaces
board = [[" " for _ in range(3)] for _ in range(3)]
display_board(board)

