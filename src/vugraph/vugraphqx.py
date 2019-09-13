
"""
Provides a room ('o' for "Open Room", or 'c' for "Closed Room") and the board number. For example:

o1
"""


class VugraphQX(object):
    def __init__(self, room, board_number):
        self.type = 'qx'
        self.room = room
        self.board_number = board_number

    @staticmethod
    def parse(qx):
        room = qx[0:1]
        if room != 'c' and room != 'o':
            raise Exception('Unrecognized room, expecting "o" or "c": ' + qx)
        board_number = int(qx[1:])
        return VugraphQX(room, board_number)

    def __eq__(self, other):
        return isinstance(other, VugraphQX) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type + ':' + self.room + ':' + str(self.board_number)
