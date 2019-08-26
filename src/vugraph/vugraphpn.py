
"""
David Souk,Julien Ber,Hakan Berk,Thibault V,Baptiste C,Cyrus Hett,Luc Bellic,Daniel Son
"""


class VugraphPN(object):
    def __init__(self, names):
        self.names = names

    @staticmethod
    def parse(pn):
        names = pn.split(',')
        if len(names) % 4 != 0:
            raise Exception('Unexpected number of names: ' + pn)
        return VugraphPN(names)

