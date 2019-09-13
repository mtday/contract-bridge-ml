
"""
No idea what information is provided by this. Haven't yet seen a non-empty value.
"""


class VugraphRH(object):
    def __init__(self):
        self.type = 'rh'

    @staticmethod
    def parse(rh):
        # Not expecting a value
        if '' != rh:
            raise Exception('Unexpected non-empty "rh" value: ' + rh)
        return VugraphRH()

    def __eq__(self, other):
        return isinstance(other, VugraphRH) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type
