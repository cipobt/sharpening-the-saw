from game_engine import GameEngine

def play_game():
    game = GameEngine()
    while True:
        game.display_board()
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
        if game.make_move(row, col):
            if game.check_win():
                game.display_board()
                print(f"Player {game.current_player} wins!")
                break
            elif game.check_draw():
                game.display_board()
                print("It's a draw!")
                break
            game.switch_player()
        else:
            print("Spot already taken. Try again.")

if __name__ == "__main__":
    play_game()
