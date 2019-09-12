
"""
No idea what this is. Have seen a few different values. Calling it "board_type" for now.

o
n
"""


class VugraphSV(object):
    def __init__(self, board_type):
        self.board_type = board_type

    @staticmethod
    def parse(sv):
        if sv != 'b' and sv != 'e' and sv != 'n' and sv != 'o':  # TODO: what is this?
            raise Exception('Unsupported board type: ' + sv)
        return VugraphSV(sv)
