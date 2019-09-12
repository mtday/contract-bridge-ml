
"""
No idea what information is provided by this. Haven't yet seen a non-empty value.
"""


class VugraphRH(object):
    def __init__(self):
        pass

    @staticmethod
    def parse(rh):
        # Not expecting a value
        if '' != rh:
            raise Exception('Unexpected non-empty "rh" value: ' + rh)
        return VugraphRH()
