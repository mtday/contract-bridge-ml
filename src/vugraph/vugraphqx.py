
"""
Provides a hand type (?) and the board number. For example:

o1
"""


class VugraphQX(object):
    def __init__(self, hand_type, board_number):
        self.hand_type = hand_type
        self.board_number = board_number

    @staticmethod
    def parse(qx):
        hand_type = qx[0:1]  # TODO: what is this?
        if hand_type != 'c' and hand_type != 'o':
            raise Exception('Unrecognized hand type: ' + qx)
        board_number = int(qx[1:])
        return VugraphQX(hand_type, board_number)
