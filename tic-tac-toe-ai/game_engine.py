class GameEngine:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        print("---------")
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("---------")

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        board = self.board
        for i in range(3):
            if all([spot == self.current_player for spot in board[i]]) or \
            all([board[j][i] == self.current_player for j in range(3)]):
                return True
        if board[0][0] == board[1][1] == board[2][2] == self.current_player or \
        board[0][2] == board[1][1] == board[2][0] == self.current_player:
            return True
        return False
