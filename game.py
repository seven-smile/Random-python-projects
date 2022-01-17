class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] # we will use a single list to rep 3x3 board
        self.current_winner = None # keep  track of winner!

    def print_board(self):
        for row in [self.board[(i + 1) * 3] for i in range(3)]:
            print(" | " + " | ".join(row) + " | ")
    

    @staticmethod
    def print_board_nums():
        # 8 | 1 | 2 | ets (tells us what number corresponds to what box)
        number_board = [[str(i)] for i in range (j*3, (j+1)*3)] for j in range (3)]
        for row in number_board:
            print(" | " + " | ".join(row) + " | ")

