
"""
+!d unbal
"""


class VugraphAN(object):
    def __init__(self, annotation):
        self.annotation = annotation

    @staticmethod
    def parse(an):
        return VugraphAN(an)
