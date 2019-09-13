
"""
Provides a comma-delimited list of player names. For example:

David Souk,Julien Ber,Hakan Berk,Thibault V,Baptiste C,Cyrus Hett,Luc Bellic,Daniel Son

The names are in order of S,W,N,E.
"""


class VugraphPN(object):
    def __init__(self, names):
        self.type = 'pn'
        self.names = names

    @staticmethod
    def parse(pn):
        names = pn.split(',')
        if len(names) % 4 != 0:
            raise Exception('Unexpected number of names: ' + pn)
        return VugraphPN(names)

    def __eq__(self, other):
        return isinstance(other, VugraphPN) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        s = self.type
        for name in self.names:
            s += ':' + name
        return s

