class GameEngine:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        print("---------")
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("---------")
