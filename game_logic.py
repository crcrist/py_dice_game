from dice import DiceRoller
from character import Player, Enemy

class GameLogic:
    def __init__(self):
        self.players = []
        self.dice_roller = None
        self.current_round = 1

    def setup_game(self):
        player_name = input(f"Enter your name player: ")
        self.players.append(Player(player_name))

        num_enemies = int(input("how many enemies will you have to play against?"))
        for i in range(num_enemies):
            self.players.append(Enemy()) # add each name to the list of players
        
        num_dice = int(input("how many dice would you like to play with?"))
        self.dice_roller = DiceRoller(num_dice)

    def player_turn(self, character):
        rerolls = 0
        while rerolls < 3:
            roll = self.dice_roller.roll()
            character.current_roll = roll
            print(f"{character.name} rolled: {roll}")

            if self.dice_roller.is_doubles() and rerolls < 2:
                if isinstance(character, Enemy):
                    print(f"{character.name} automatically rerolls!")
                    rerolls += 1
                    continue
                else: # human player
                    reroll = input("you rolled doubles! roll again? (y/n): ")
                    if reroll.lower() == "y":
                        rerolls += 1
                        continue

            character.add_to_score(roll)
            break

    def play_round(self):
        print(f"\nRound {self.current_round}")
        for character in self.players:
            self.player_turn(character)

        self.show_scores()
        winner = max(self.players, key = lambda x: x.score) # finding the player with the highest score. max() for highest value, the key = lambda x: x.score is saying to compare max based on score attribute.
        print(f"winner of round {self.current_round} is {winner.name} with {winner.score} points!")

        if input("Play another round? (y/n): ").lower() == 'y':
            self.current_round += 1 
            return True
        return False

    def show_scores(self):
        print("\nCurrent Scores:")
        for character in self.players:
            print(f"{character.name}: {character.score}")

    def play_game(self):
        self.setup_game()
        while self.play_round():
            pass

        winner = max(self.players, key = lambda x: x.score)
        print(f"\nGame Over! Winner is {winner.name} with {winner.score} points!")


