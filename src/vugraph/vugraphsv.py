
"""
No idea what this is. Have seen a few different values. Calling it "board_type" for now.

o
n
"""


class VugraphSV(object):
    def __init__(self, board_type):
        self.type = 'sv'
        self.board_type = board_type

    @staticmethod
    def parse(sv):
        if sv != 'b' and sv != 'e' and sv != 'n' and sv != 'o':  # TODO: what is this?
            raise Exception('Unsupported board type: ' + sv)
        return VugraphSV(sv)

    def __eq__(self, other):
        return isinstance(other, VugraphSV) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type + ':' + self.board_type
