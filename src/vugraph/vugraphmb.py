
from model import Bid

"""
Provides a bid that was made by a player. For example:

p
3c
"""


class VugraphMB(object):
    def __init__(self, bid):
        self.type = 'mb'
        self.bid = bid

    @staticmethod
    def parse(mb):
        return VugraphMB(Bid.parse(mb))

    def __eq__(self, other):
        return isinstance(other, VugraphMB) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type + ':' + str(self.bid)
