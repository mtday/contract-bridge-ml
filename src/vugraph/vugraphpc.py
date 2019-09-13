
from model import Card

"""
Represents a card being played. For example:

c3
"""


class VugraphPC(object):
    def __init__(self, card):
        self.type = 'pc'
        self.card = card

    @staticmethod
    def parse(pc):
        return VugraphPC(Card.parse(pc))

    def __eq__(self, other):
        return isinstance(other, VugraphPC) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type + ':' + str(self.card)
