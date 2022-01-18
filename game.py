from lib2to3.pytree import LeafPattern
from re import T


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

    def available_moves(self):
        return [ i for i, spot in enumerate(self.board) if spot == " "]
        
        def empty_squares(self):
            return " " in self.board

        def num_empty_squares(self):
            return len(self.available_moves())  # or return self.board.count(" ") to return the number of counts left. 
        
        def make_move(self, square, letter):
            # if valid move, then make the move (assign square to letter)
            # then return true. if invalid, return false
            if self.board[square] == " ":
                self.board[square] == letter 
                return True
            else:
                return False

        
        # moves == []
        # for (i, spot) in enumerate[self.board]:
        #      # ['x', 'x', "o"] --> [(0, "x"), (1, 'x'), (2,"o")]
        #      if spot == " ":
        #            moves.append(i)
        #return moves
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X" # for starting letter
    # iterate while the game still has empty squares.
    #we don'thave to worry about winners beacuse we'll just return that 
    #which breaks the loop
    while game.empty_squares():
        # to get the move from the appropriate player
        if  letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)