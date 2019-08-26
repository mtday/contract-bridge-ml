

class VugraphPG(object):
    def __init__(self):
        pass

    @staticmethod
    def parse(pg):
        # Not expecting a value
        if '' != pg:
            raise Exception('Unexpected non-empty "pg" value: ' + pg)
        return VugraphPG()
