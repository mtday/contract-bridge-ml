
from model import Card

"""
Represents a card being played. For example:

c3
"""


class VugraphPC(object):
    def __init__(self, card):
        self.card = card

    @staticmethod
    def parse(pc):
        return VugraphPC(Card.parse(pc))
