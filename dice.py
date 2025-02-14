import random

class DiceRoller:
    def __init__(self, num_dice):
        self.num_dice = num_dice
        self.last_roll = []
    
    def roll(self):
        self.last_roll = [random.randint(1,6) for _ in range(self.num_dice)] # list comprehension; creates a list of random numbers num_dice length long. _ is used because we do not need to keep track of # of iterations
        return self.last_roll
    
    def is_doubles(self):
        return len(set(self.last_roll)) == 1 # set() is used to create a unique list of values, if [1, 1, 2] then result is [1, 2]. len() is used to make sure only 1 unique number, meaning all rolls are the same.


