
"""
No idea what information is provided by this. Haven't yet seen a non-empty value.
"""


class VugraphST(object):
    def __init__(self):
        pass

    @staticmethod
    def parse(st):
        # Not expecting a value
        if '' != st:
            raise Exception('Unexpected non-empty "st" value: ' + st)
        return VugraphST()
