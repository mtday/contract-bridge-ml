
from model import Bid

"""
p
3c
"""


class VugraphMB(object):
    def __init__(self, bid):
        self.bid = bid

    @staticmethod
    def parse(mb):
        return VugraphMB(Bid.parse(mb))
