from player import GeniusComputerPlayer, HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] # we will use a single list to rep 3x3 board
        self.current_winner = None # keep  track of winner!

    def print_board(self):
        for row in [self.board[i*3:(i + 1)*3] for i in range(3)]:
            print(" | " + " | ".join(row) + " | ")
    

    @staticmethod
    def print_board_nums():
        # 8 | 1 | 2 | ets (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range (j*3, (j+1)*3)] for j in range (3)]
        for row in number_board:
            print(" | " + " | ".join(row) + " | ")

    def available_moves(self):
        return [ i for i, spot in enumerate(self.board) if spot == " "]
        
    def empty_squares(self):
            return " " in self.board

    def num_empty_squares(self):
            return self.board.count(" ")  # or len(self.available_moves() to return the number of counts left. 
        
    def make_move(self, square, letter):
            # if valid move, then make the move (assign square to letter)
            # then return true. if invalid, return false
            if self.board[square] == " ":
                self.board[square] == letter
                if self.winner(square, letter):
                    self.current_winner = letter
                return True
            return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere. we have to check all of these!
        # firdt we check the row
        row_ind = square // 3
        row  = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check Column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)] 
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        #thes are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all these checks fail
        return False
            
        
        # moves == []
        # for (i, spot) in enumerate[self.board]:
        #      # ['x', 'x', "o"] --> [(0, "x"), (1, 'x'), (2,"o")]
        #      if spot == " ":
        #            moves.append(i)
        #return moves


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game(the letter). or None for a tie
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

        # let's define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f"makes a move to square{square}")
                game.print_board()
                print("" )# just empty line)

            if game.current_winner:
                if print_game:
                    print(letter + "wins!")
                return letter 


            # after we have made our move, we need to alternate leters.
            letter = "O" if letter == "X" else "X" # switch player
            # if  letter == "X":
            #       letter - "O"
            #else:
            #    letter  = "X"

        if print_game:
            print("It\'s a tie")
    if print_game:
        print{"It\'s a tie!"}


if __name__ == "_main_":
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000): 
        x_player = RandomComputerPlayer("X")
        o_player = GeniusComputerPlayer("O")
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins += 1
        elif result == 0:
            o_wins += 1
        else:
            ties += 1
    print(f'After 1000 iteratins \, we see that {x_wins} Xwins,{o_wins} O wins, and {ties} ties')