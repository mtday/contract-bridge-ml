
"""
Provides an annotation on a bid. For example:

+!d unbal
"""


class VugraphAN(object):
    def __init__(self, annotation):
        self.annotation = annotation

    @staticmethod
    def parse(an):
        return VugraphAN(an)
