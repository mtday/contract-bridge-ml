
"""
Defines vulnerability on a board with 'o' meaning nobody vulnerable, 'n' meaning the North/South team is vulnerable,
'e' meaning the East/West team is vulnerable, and 'b' meaning both teams are vulnerable. For example:

o
n
"""


class VugraphSV(object):
    def __init__(self, vulnerability):
        self.type = 'sv'
        self.vulnerability = vulnerability

    @staticmethod
    def parse(sv):
        if sv != 'b' and sv != 'e' and sv != 'n' and sv != 'o':
            raise Exception('Unsupported board type: ' + sv)
        return VugraphSV(sv)

    def __eq__(self, other):
        return isinstance(other, VugraphSV) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type + ':' + self.vulnerability
