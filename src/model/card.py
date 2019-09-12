
import re

"""
Supports parsing and representing a single card.
"""


class Card(object):
    SUITS = {'c': 0, 'd': 1, 'h': 2, 's': 3}
    LEVELS = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7,
              't': 8, 'j': 9, 'q': 10, 'k': 11, 'a': 12}

    def __init__(self, suit, level):
        self.suit = suit
        self.level = level

    @staticmethod
    def parse(value):
        lower = value.lower()
        if not re.match('^[cdhs][2-9tjqka]$', lower):
            raise Exception('Invalid card: ' + value)
        return Card(lower[0], lower[1])

    def order(self):
        return self.SUITS[self.suit] * 13 + self.LEVELS[self.level]

    def __eq__(self, other):
        return isinstance(other, Card) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.suit + self.level
