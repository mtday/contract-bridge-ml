
"""
Provides a hand type (?) and the board number. For example:

o1
"""


class VugraphQX(object):
    def __init__(self, hand_type, board_number):
        self.type = 'qx'
        self.hand_type = hand_type
        self.board_number = board_number

    @staticmethod
    def parse(qx):
        hand_type = qx[0:1]  # TODO: what is this?
        if hand_type != 'c' and hand_type != 'o':
            raise Exception('Unrecognized hand type: ' + qx)
        board_number = int(qx[1:])
        return VugraphQX(hand_type, board_number)

    def __eq__(self, other):
        return isinstance(other, VugraphQX) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type + ':' + self.hand_type + ':' + str(self.board_number)
