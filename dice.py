import random
import time

def dice_roll(player):
    """ this method simulates a dice roll, by showing numbers 1 through 6 for half a second by using the time.sleep() method,
        then prints the return of the roll with the statement below. I am requiring player to be input as an argument, because it is assumed
        only one player can roll the dice at a time."""

    print(f"\nrolling for {player}..")
    # print 5 random ints over half a second
    for i in range(5): 
        number = random.randint(1, 6) 
        print(number)
        time.sleep(0.5)

    # assign the actual roll to the score 
    score = random.randint(1,6)    
    # print the players score
    print(f"{player} rolled a {score}!\n")

    return score
