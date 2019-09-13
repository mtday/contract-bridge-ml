
"""
No idea what information is provided by this. Haven't yet seen a non-empty value.
"""


class VugraphST(object):
    def __init__(self):
        self.type = 'st'

    @staticmethod
    def parse(st):
        # Not expecting a value
        if '' != st:
            raise Exception('Unexpected non-empty "st" value: ' + st)
        return VugraphST()

    def __eq__(self, other):
        return isinstance(other, VugraphST) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type
