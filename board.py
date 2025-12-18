class Board:
    def __init__(self):
        self.board = [[" " for x in range(3)] for y in range(3)]
        self.empty_line = "   "

    def draw_board(self):
        print("-------------")
        for z in range(3):
            print("|" + self.empty_line + "|" + self.empty_line + "|" + self.empty_line + "|")
            print("| " + self.board[z][0] + " | " + self.board[z][1] + " | " + self.board[z][2] + " |")
            print("|" + self.empty_line + "|" + self.empty_line + "|" + self.empty_line + "|")
            print("-------------")

    def add_to_board(self, x_cord, y_cord, player):
        if self.board[x_cord][y_cord] == " ":
            self.board[x_cord][y_cord] = player
            return True
        else:
            return False