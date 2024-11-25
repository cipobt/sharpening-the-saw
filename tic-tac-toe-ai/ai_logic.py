import time

def get_available_moves(board):
    """Returns a list of available spots on the board."""
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]


def minimax(board, current_player, ai_symbol, player_symbol, depth, is_maximizing, max_depth):
    """
    Minimax algorithm to find the optimal move for the AI, factoring in depth for faster wins or slower losses.

    Args:
        board (list): Current state of the game board.
        current_player (str): Current player's symbol ('X' or 'O').
        ai_symbol (str): AI's symbol ('X' or 'O').
        player_symbol (str): Opponent's symbol.
        depth (int): Depth of the recursive search.
        is_maximizing (bool): True if the AI is maximizing its score, False if minimizing.
        max_depth (int): Maximum depth for recursion to limit computational effort.

    Returns:
        int: The score of the board after the best possible move.
    """
    # Check win/draw conditions
    if current_player == ai_symbol and check_win(board, ai_symbol):
        return 10 - depth
    elif current_player == player_symbol and check_win(board, player_symbol):
        return depth - 10
    elif check_draw(board):
        return 0

    if depth >= max_depth:
        return 0  # Neutral score at maximum depth

    # Minimax logic
    if is_maximizing:
        best_score = -float('inf')
        for (row, col) in get_available_moves(board):
            board[row][col] = ai_symbol
            score = minimax(board, player_symbol, ai_symbol, player_symbol, depth + 1, False, max_depth)
            board[row][col] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for (row, col) in get_available_moves(board):
            board[row][col] = player_symbol
            score = minimax(board, ai_symbol, ai_symbol, player_symbol, depth + 1, True, max_depth)
            board[row][col] = " "
            best_score = min(score, best_score)
        return best_score


def ai_move(board, ai_symbol, player_symbol, difficulty="Medium"):
    """
    Determines the best move for the AI using a combination of immediate checks and the Minimax algorithm.

    Args:
        board (list): Current state of the game board.
        ai_symbol (str): AI's symbol ('X' or 'O').
        player_symbol (str): Opponent's symbol.
        difficulty (str): AI difficulty level ("Easy", "Medium", "Hard").

    Returns:
        tuple: The (row, col) position of the AI's move.
    """
    # Define depth levels based on difficulty
    depth_map = {"Easy": 1, "Medium": 3, "Hard": 6}
    max_depth = depth_map.get(difficulty, 3)

    print(f"AI ({difficulty} mode) is thinking...")
    time.sleep(1.5)

    # Step 1: Check for immediate winning move
    for (row, col) in get_available_moves(board):
        board[row][col] = ai_symbol
        if check_win(board, ai_symbol):
            board[row][col] = " "  # Reset the board before returning
            return row, col  # Execute the winning move immediately
        board[row][col] = " "  # Reset the board if no win is found

    # Step 2: Use Minimax to calculate the best strategic move
    best_score = -float('inf')
    best_move = None
    for (row, col) in get_available_moves(board):
        board[row][col] = ai_symbol  # Simulate the move
        score = minimax(
            board=board,
            current_player=player_symbol,
            ai_symbol=ai_symbol,
            player_symbol=player_symbol,
            depth=0,
            is_maximizing=False,
            max_depth=max_depth,
        )
        board[row][col] = " "  # Undo the move
        if score > best_score:
            best_score = score
            best_move = (row, col)  # Update the best move

    return best_move  # Return the best move determined
