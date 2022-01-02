from random import randint
class Die:
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

    def roll(self): #uses randint func
        return randint(1, self.num_sides) #returns random number between 1 and number of sides