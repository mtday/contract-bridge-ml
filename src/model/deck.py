
from .card import Card

"""
Provides a complete deck of cards.
"""


class Deck(object):
    @staticmethod
    def cards():
        cards = []
        for suit in Card.SUITS.keys():
            for value in Card.LEVELS.keys():
                cards.append(Card(suit, value))
        return cards
