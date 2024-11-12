def choose_symbol():
    """Prompts the player to choose their symbol and returns 'X' or 'O'."""
    symbol = input("Choose your symbol (X or O): ").upper()
    return symbol if symbol in ["X", "O"] else "X"
