from math import floor
import random


def d6():
    return random.randint(1, 6)


def attribute():
    results = [d6() for i in range(0, 4)]
    return sum(sorted(results)[1:])


def modifier(constitution):
    return floor((constitution - 10) / 2)


class Character:
    def __init__(self):
        self.strength = attribute()
        self.dexterity = attribute()
        self.constitution = attribute()
        self.intelligence = attribute()
        self.wisdom = attribute()
        self.charisma = attribute()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self, ability=None):
        if not ability:
            abilities = [
                'strength',
                'dexterity',
                'constitution',
                'intelligence',
                'wisdom',
                'charisma',
            ]
            ability = random.choice(abilities)
        return getattr(self, ability)
