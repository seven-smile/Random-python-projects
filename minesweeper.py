import random
# lets create a board objects to represent the minesweeper game
# this is so that we can say "create a new board object", or
# "dig here", or " render this game for this object"

class Board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters. they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #let's create the board
        #helper function
        self.board = self.make_new_baord() # plan the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        #we'll save (row, col) tuples into this set
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}


    def make_new_board(self):
        # construst a new board based on the dim_size an num_bombs 
        # we would construct the list of list here ( or what ever representstions prefered,
        # but since we have a 2-D board, list of list is most natural)

        #generate a new board
        board = [[None for _ in range (self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ..., None],
        # [None, None, ...., None],
        # [...                   ],
        # [None, None, ...., None]]
        # we can see how this represents a board!

        # plant the bombs
        bombs_planted = 0
        while bombs_planted <self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1) # returns a random integer N such that a <= N <= b
            row = loc // self.dim_size # we want the number of times dim_size goes into the loc to tell us
            col = loc % self.dim_size # we want the remainder to tell us what idex in that row to loc

            if board[row][col] == '*':
                #this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] == "*" # plant the bomb
            bombs_planted +=1
        return board


# play the game
def play(dim_size = 10, num_bombs=10):
        # step 1: create the board and plant the bombs
        # step 2: show the user the board and ask them where they would like to dig
        # step 3a: if location is a bomb, show game-over message
        # step 3b:  if location isnot a bomb,dig recursivly untileach square is a t least next to a bomb
        # step 4: repeat step 2 and 3a/b until there are no more places to dig --> VICTORY!!!
        pass 