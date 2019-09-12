
"""
Provides the total number of tricks taken by declarer in a hand. For example:

10
"""


class VugraphMC(object):
    def __init__(self, tricks_taken):
        self.tricks_taken = tricks_taken

    @staticmethod
    def parse(mc):
        tricks_taken = int(mc)
        if tricks_taken < 0 or tricks_taken > 13:
            raise Exception('Invalid number of tricks taken: ' + mc)
        return VugraphMC(tricks_taken)
