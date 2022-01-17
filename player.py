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
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass