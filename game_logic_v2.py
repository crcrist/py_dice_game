from player import find_players, find_winner, track_total_score
from termcolor import colored # importing colors here for fun to show the round winner and game winners score in green
from dice import dice_roll

def start_game():
    """
    This method starts the game, it is simply asking how many players will be playing, and returns the number of players and each of their names
    """
    # this try catch block is used here to make sure the user inputs an integer
    while True:
        try:
            no_players = int(input("how many players will be playing dice?\n"))
            break
        except ValueError:
            print("please enter a number!\n")
    # use the find players method to find each of the players names
    players = find_players(no_players)
    
    return no_players, players

def game_play(no_players, players, round_count):
    """
    This gameplay method holds most of the game logic. The game operates as so:
    1. You start off with an initial roll of two dice
    2. If you roll a double, you get to roll again
    3. You can get a maximum of 3 rolls, you can also decline to reroll
    4. Transparently this logic can be simplified, however I wanted the print statements to show correctly for each outcome, 
    so that there was no redundant scores showing etc.
    5. At the end of each round the round winner is displayed, 
    as well as the winner of the game so far, the user is then prompted if they want to continue playing or not.

    """
    print(f"\nyou are on round {round_count}\n")
    # make an empty array of final scores
    final_score = [0] * no_players
    for i in range(0, len(players)):
        # the first roll starts here
        dice_roll_1 = dice_roll(players[i])
        dice_roll_2 = dice_roll(players[i])
        score = dice_roll_1 + dice_roll_2
        roll_count = 1

        # if a double is rolled, the player enters into this loop. Ask if they want to roll again, y for yes n for no
        while dice_roll_1 == dice_roll_2 and roll_count < 3:
            roll_again = input(f"{players[i]}, you just rolled a double {dice_roll_1}, giving you a score of {score}! Since you rolled a double, you can roll again.\nWould you like to roll again? Enter y for yes or n for no.\n").lower()

            """
            - if we wanted to add some additional functionality such as rolling a double 4 is actually worth 20 points or 1 point, that could be done here, 
            by assigning the score variable a hard-coded value, and by using an if statement if dice_roll_1 == dice_roll_2 and dice_roll_1 == 4
            - for simplicity i just kept the doubles as their actual values.
            """


            # validate the input is y or n, if not keep asking
            while roll_again != "y" and roll_again != "n":
                roll_again = input("please enter 'y' for yes or 'n' for no\n").lower()

            # if user does not want to roll again, break loop
            if roll_again == "n":
                # this would have been the second roll, the user already knows what their current score is so no need to tell them in the loop below
                roll_count += 1
                final_score[i] = score
                break
            
            # user wants to roll again, so they enter this loop. The player can only reroll 3 times 
            while roll_again == "y" and roll_count < 3:
                dice_roll_1 = dice_roll(players[i])
                dice_roll_2 = dice_roll(players[i])
                score += dice_roll_1 + dice_roll_2
                roll_count += 1
                # the user has rolled again, so they must decide again whether they want another reroll (if they get a double), this sends them back to the outermost loop. Save the score in case they opt out of reroll.
                roll_again = "n"
                final_score[i] = score

                # player rerolled but the reroll was not a double, we want to display their score properly
                if dice_roll_1 != dice_roll_2:
                    print(f"{players[i]}, you rolled a {dice_roll_1} and a {dice_roll_2}, giving you a total score of {score}.")                   
                
                # if it is the 3rd reroll, enter here
                if roll_count == 3:
                    print(f"{players[i]}, your final score is {score}, you just had your final roll of {roll_count} rolls. Hope the number was good!")
                    final_score[i] = score

    
        # player did not roll a double    
        if roll_count == 1:
            print(f"{players[i]}, you rolled a {dice_roll_1} and a {dice_roll_2}, giving you a score of {score}.")
            final_score[i] = score

    # find the highest score in order to find the winner
    highest_score = max(final_score)
                
    return players, final_score, highest_score

if __name__ == "__main__":
    """
    In the main function all functions are brought together, the flow of the program is as such:
    1. the game_active flag is true at default as we assume the player is wanting to play the game if they have ran the application, while in this loop
    the game will continue. At the end of each round the player has the ability to break the loop and end the game. 
    2. 
    """
    game_active = True # flag starts as true
    round_count = 1 # we start on round 1

    no_players, players = start_game() # number of players and their names returned from this function


    total_score = [0] * len(players) # initialize the total scores array

    # while the game is going on, this loop is running
    while game_active:

        # get the players final scores for each round with this method
        players, final_score, highest_score = game_play(no_players, players, round_count)

        # find the winner of each round with this method, then print the winners (also print multiple winners if there is a tie)
        winner, round_count, highest_score = find_winner(players, final_score, highest_score, round_count)
        # if there is more than one winner there must have been a tie, if not print one winner
        if len(winner) > 1:
            print(f"\nthere was a tie between", end = ' ') 
            print(*winner, sep =', ', end = '')
            # add green color to the score of the winners
            print(f", these players won round {round_count} with a score of {colored(highest_score, 'green')}")
        else:
            print(f"\ncongratulations", end = ' ')
            print(*winner, sep= ', ', end = '')
            print(f", you won round {round_count} with a score of {colored(highest_score, 'green')}")

        # find the players total game score with this method
        total_score = track_total_score(players, final_score, round_count, total_score)

        # find the highest total score with the following method
        highest_total_score = max(total_score)

        # use the same find_winner() method to find the winner of the game instead of just the round
        total_winner, round_count, total_highest_scoure = find_winner(players, total_score, highest_total_score, round_count)
        if len(total_winner) > 1:
            print(f"\nthere is currently a tie between", end = ' ')
            print(*total_winner, sep= ', ', end = '')
            print(f" to win the game, with a score of {colored(highest_total_score, 'green')}!")    
        else:
            print(f"\nthe current leader of the game is", end = ' ')
            print(*total_winner, sep= ', ', end = '')
            print(f", with a score of {colored(highest_total_score, 'green')}!")    

        # prompt the user to see if they want to play another game
        continue_game = input("\nwould you like to play another round? select y for yes and n for no\n").lower()

        # make sure they only enter 'y' or 'n'
        while continue_game != "y" and continue_game != "n":
            continue_game = input("please enter 'y' for yes or 'n' for no\n").lower()

        # if the game ends, print the winners of the game and say congratulations
        if continue_game == 'n':
            print(f"\ncongratulations", end = ' ')
            print(*total_winner, sep= ', ', end = '')
            print(f", you won the game with a score of {colored(highest_total_score, 'green')}!") 
            game_active = False
    
        else:
            round_count += 1

