
"""
Provides the total number of tricks taken by declarer in a hand. For example:

10
"""


class VugraphMC(object):
    def __init__(self, tricks_taken):
        self.type = 'mc'
        self.tricks_taken = tricks_taken

    @staticmethod
    def parse(mc):
        tricks_taken = int(mc)
        if tricks_taken < 0 or tricks_taken > 13:
            raise Exception('Invalid number of tricks taken: ' + mc)
        return VugraphMC(tricks_taken)

    def __eq__(self, other):
        return isinstance(other, VugraphMC) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type + ':' + str(self.tricks_taken)
