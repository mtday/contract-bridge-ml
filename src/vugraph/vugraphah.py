
"""
Provides a description of the board. For example:

Board 1
"""


class VugraphAH(object):
    def __init__(self, description):
        self.type = 'ah'
        self.description = description

    @staticmethod
    def parse(ah):
        return VugraphAH(ah)

    def __eq__(self, other):
        return isinstance(other, VugraphAH) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type + ':' + self.description
