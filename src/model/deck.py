
from .card import Card


class Deck(object):
    @staticmethod
    def cards():
        cards = []
        for suit in Card.SUITS.keys():
            for value in Card.LEVELS.keys():
                cards.append(Card(suit, value))
        return cards
