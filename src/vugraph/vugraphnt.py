
"""
vugraphe1: N asks EW's defence to 1NT
"""


class VugraphNT(object):
    def __init__(self, note):
        self.note = note

    @staticmethod
    def parse(nt):
        return VugraphNT(nt)
