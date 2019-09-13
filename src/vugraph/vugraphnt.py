
"""
Provides a note that describes more information about what is happening. For example:

vugraphe1: N asks EW's defence to 1NT
"""


class VugraphNT(object):
    def __init__(self, note):
        self.type = 'nt'
        self.note = note

    @staticmethod
    def parse(nt):
        return VugraphNT(nt)

    def __eq__(self, other):
        return isinstance(other, VugraphNT) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type + ':' + self.note
