
def find_players(no_players):
    """this method takes in the number of players as an argument, then asks the names of that many number of players. 
    For example if find_players(3) the method will ask 3 players htheir name"""
    
    # create an empty array of length number of players long
    players = [0] * no_players
    # for each player
    for i in range(0, no_players):
        
        # ask their name
        player_name = input(f"""\nPlayer {i + 1}, what is your name?\n""")
        print(f"""welcome {player_name}
        """)
        # assign their name to the array of players
        players[i] = player_name

    # print out the included players
    print("players included in this game are", end = ' ') 
    print(*players, sep=', ', end = '') 
    print(", good luck!")

    return players


def find_winner(players, final_score, highest_score, round_count):
    """This method finds the winner for each round by comparing each of the players final scores against the highest score. 
    If the players final score is the highest, they are the winner."""
    # initialize empty array
    winner = []
    # for each of the players final score, see if it is equivalent to the highest score
    for i in range(0, len(final_score)):
        if final_score[i] == highest_score:
            # i am using append here in case their are ties amongst the players, if the players score is the highest, append it to the winner array
            winner.append(players[i])

    return winner, round_count, highest_score
                

def track_total_score(players, final_score, round_count, total_score):
    """ This method tracks the total score of each of the players for the whole game, 
    by adding their final score at the end of the round, to their total game score."""

    print(f"\nat the end of round {round_count} total scores for each player are..")
    # for each of the players final score, add it to their total score
    for i in range(0, len(final_score)):
        total_score[i] += final_score[i]
        print(f"{players[i]} : {total_score[i]}") 

    return total_score

