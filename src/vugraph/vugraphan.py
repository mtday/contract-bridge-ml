
"""
Provides an annotation on a bid. For example:

+!d unbal
"""


class VugraphAN(object):
    def __init__(self, annotation):
        self.type = 'an'
        self.annotation = annotation

    @staticmethod
    def parse(an):
        return VugraphAN(an)

    def __eq__(self, other):
        return isinstance(other, VugraphAN) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.type + ':' + self.annotation
