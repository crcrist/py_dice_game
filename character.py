import random

ENEMY_ADJECTIVES = ["Dark", "Shadow", "Mystic", "Chaos", "Ancient", "Crystal", "Storm", "Void", "Ghost", "Iron"]
ENEMY_NOUNS = ["Knight", "Warrior", "Rogue", "Mage", "Hunter", "Dragon", "Phoenix", "Titan", "Specter", "Guardian"]

class Character:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current_roll = []
    
    def add_to_score(self, points):
        self.score += sum(points)

class Player(Character):
    def __init__(self, name):
        super().__init__(name)


class Enemy(Character):
    def __init__(self):
        adjective = random.choice(ENEMY_ADJECTIVES)
        noun = random.choice(ENEMY_NOUNS)
        name = f"{adjective} {noun}"
        super().__init__(name)


