
import re

"""
Supports parsing and representing the final contract played for a board.
"""


class Contract(object):
    def __init__(self, level=None, suit=None, declarer=None, doubled=False, redoubled=False, passout=False):
        self.level = level
        self.suit = suit
        self.declarer = declarer
        self.doubled = doubled
        self.redoubled = redoubled
        self.passout = passout

    @staticmethod
    def parse(value):
        lower = value.lower()
        if not re.match('^[1-7][cdhsn][nsew]x{0,2}$', lower):
            raise Exception('Invalid contract: ' + value)
        level = lower[0]
        suit = lower[1]
        declarer = lower[2]
        doubled = bool(re.match('^[1-7][cdhsn][nsew]x$', lower))
        redoubled = bool(re.match('^[1-7][cdhsn][nsew]xx$', lower))
        passout = bool(re.match('^passout$', lower))
        return Contract(level, suit, declarer, doubled, redoubled, passout)

    def __eq__(self, other):
        return isinstance(other, Contract) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        if self.passout:
            return 'passout'
        rep = self.level + self.suit + self.declarer
        if self.doubled:
            rep = rep + 'x'
        elif self.redoubled:
            rep = rep + 'xx'
        return rep
