import math
import random
class Player:
    def __init__(self, letter):
        # letter is x or 0 
        self.letter = letter

        #we want all players to get thier next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square
        
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\"s turn. Input move(0-8):")
            # we are going to check that this is a correct value by trying to cast 
            # it to an integer, and if it's not, then we say it's invalid
            #if that spot is not available on the board, we also say it's invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are succesful,then yay!
            except ValueError:
                print('invalid square. Try again.')
        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_move()) == 9:
            square = random.choice(game.available_moves()) # randomly choose one
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square


    def minimax(self,state, player):
            max_player = self.letter # yourself! 
            other_player = 'O' if player == 'X' else 'X' # the other player

            # first, we want to check if the privious move is a winner
            # this is our base case
            if state.current_winner == other_player:
                # we should return position and score because we need to keep track of the score
                # for minimax to work
                return {'position ': None,
                        'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 *
                        (state.num_empty_square() + 1) }
                    
            elif not state.empty_squares(): # no empty squares
                    return { 'position': None, 'score': 0}
                
            # initialize score dictionaries
            if player == max_player:
                best = { 'position': None, 'score': -math.inf} # each score should maximize ( the largest)


            for possible_move in state.available_moves():
                # step 1: make amove and try that spot
                state.make_move(possible_move, player)
                # step 2: recurse using minimax to simulate a game after making that move
                sim_score = self.minimax(state, other_player) # now we altenate players

                # step 3: we undo te move
                state.board[possible_move] = " "
                state.current_winner = None
                sim_score ['position'] = possible_move # otherwise this would get messed up from the top

                # step 4: update the dictionaries if neccesary
                if player == max_player: #we are trying to maximize the max_player
                    if sim_score['score'] > best['score']:
                        best = sim_score # this is to replace the best

            return best