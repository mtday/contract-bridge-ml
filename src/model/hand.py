
from .card import Card
import re


class Hand(object):
    def __init__(self, card_list):
        self.cards = card_list
        self.cards.sort(key=lambda c: c.order())
        self.card_dict = {'c': [], 'd': [], 'h': [], 's': []}
        for card in self.cards:
            self.card_dict[card.suit].append(card)

    @staticmethod
    def parse(value):
        lower = value.lower()
        if not re.match('^[cdhs2-9tjqka]+$', lower):
            raise Exception('Invalid hand: ' + value)

        # Turn the value into a list of cards
        cards = []
        chars = [char for char in lower]
        suit = None
        for char in chars:
            if re.match('^[cdhs]$', char):
                suit = char
            elif suit is not None:
                cards.append(Card(suit, char))
        if len(cards) != 13:
            raise Exception('Invalid hand has {} cards'.format(len(cards)))
        return Hand(cards)

    def __eq__(self, other):
        return isinstance(other, Hand) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        rep = ''
        for suit in self.card_dict.keys():
            cards_in_suit = self.card_dict[suit]
            if len(cards_in_suit) > 0:
                rep = rep + suit
                for card in cards_in_suit:
                    rep = rep + card.level
        return rep
