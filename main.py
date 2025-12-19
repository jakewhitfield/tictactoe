from board import Board

board = Board()
game_running = True

def player_turn(player_symbol):
    board.draw_board()
    print("It is now the '" + player_symbol + "' player's turn")

    invalid_turn = True
    while invalid_turn:
        x_coord_not_valid = True
        while x_coord_not_valid:
            x = int(input("Enter the row number (0-2): "))
            if x < 0 or x > 2:
                print("Please enter a valid column number")
            else:
                x_coord_not_valid = False
        y_coord_not_valid = True
        while y_coord_not_valid:
            y = int(input("Enter the column number (0-2): "))
            if y < 0 or y > 2:
                print("Please enter a valid row number")
            else:
                y_coord_not_valid = False

        if board.add_to_board(x_coord=x, y_coord=y, player=player_symbol):
            invalid_turn = False
            game_message = board.check_game_end()
            if game_message != "":
                board.draw_board()
                print(game_message)
                return False
        else:
            print("That space is full, please choose another space")

    return True

while game_running:
    game_running = player_turn("O")
    if game_running:
        game_running = player_turn("X")