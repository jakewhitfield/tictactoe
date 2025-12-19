class Board:
    def __init__(self):
        self.board = [[" " for x in range(3)] for y in range(3)]
        self.empty_line = "     "
        self.turns_completed = 0

    def draw_board(self):
        print("-------------------")
        for z in range(3):
            # print("|" + self.empty_line + "|" + self.empty_line + "|" + self.empty_line + "|")
            print("|  " + self.board[z][0] + "  |  " + self.board[z][1] + "  |  " + self.board[z][2] + "  |")
            # print("|" + self.empty_line + "|" + self.empty_line + "|" + self.empty_line + "|")
            print("-------------------")

    def add_to_board(self, x_coord, y_coord, player):
        if self.board[x_coord][y_coord] == " ":
            self.board[x_coord][y_coord] = player
            self.turns_completed += 1
            return True
        else:
            return False

    def check_game_end(self):
        if self.board[0][0] != " ":
            if self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][2]:
                return self.board[0][0] + " has won the game!"
            elif self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0]:
                return self.board[0][0] + " has won the game!"
            elif self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
                return self.board[0][0] + " has won the game!"

        if self.board[0][1] != " ":
            if self.board[0][1] == self.board[1][1] and self.board[0][1] == self.board[2][1]:
                return self.board[0][1] + " has won the game!"

        if self.board[0][2] != " ":
            if self.board[0][2] == self.board[1][2] and self.board[0][2] == self.board[2][2]:
                return self.board[0][2] + " has won the game!"

        if self.board[1][0] != " ":
            if self.board[1][0] == self.board[1][1] and self.board[1][0] == self.board[1][2]:
                return self.board[1][0] + " has won the game!"

        if self.board[2][0] != " ":
            if self.board[2][0] == self.board[2][1] and self.board[2][0] == self.board[2][2]:
                return self.board[2][0] + " has won the game!"
            elif self.board[2][0] == self.board[1][1] and self.board[2][0] == self.board[0][2]:
                return self.board[2][0] + " has won the game!"

        if self.turns_completed == 9:
            return "The game has ended in a draw!"

        return ""