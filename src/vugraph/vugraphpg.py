
"""
No idea what information is provided by this. Haven't yet seen a non-empty value. Seems like these are used to indicate
a new line is starting in the file but not sure.
"""


class VugraphPG(object):
    def __init__(self):
        pass

    @staticmethod
    def parse(pg):
        # Not expecting a value
        if '' != pg:
            raise Exception('Unexpected non-empty "pg" value: ' + pg)
        return VugraphPG()
