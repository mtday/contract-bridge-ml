
from model import Bid

"""
Provides a bid that was made by a player. For example:

p
3c
"""


class VugraphMB(object):
    def __init__(self, bid):
        self.bid = bid

    @staticmethod
    def parse(mb):
        return VugraphMB(Bid.parse(mb))
