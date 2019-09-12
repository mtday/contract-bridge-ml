
"""
Provides a description of the board. For example:

Board 1
"""


class VugraphAH(object):
    def __init__(self, description):
        self.description = description

    @staticmethod
    def parse(ah):
        return VugraphAH(ah)
