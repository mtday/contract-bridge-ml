
from model import Card

"""
c3
"""


class VugraphPC(object):
    def __init__(self, card):
        self.card = card

    @staticmethod
    def parse(pc):
        return VugraphPC(Card.parse(pc))
