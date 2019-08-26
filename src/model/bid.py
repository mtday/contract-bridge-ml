
import re


class Bid(object):
    def __init__(self,
                 level=None,
                 suit=None,
                 is_pass=False,
                 is_double=False,
                 is_redouble=False,
                 has_alert=False,
                 annotation=None):
        self.level = level
        self.suit = suit
        self.is_contract = level is not None and suit is not None
        self.is_pass = is_pass
        self.is_double = is_double
        self.is_redouble = is_redouble
        self.has_alert = has_alert
        self.annotation = annotation

    @staticmethod
    def parse(value):
        lower = value.lower()
        if re.match('^[1-7][cdhsn]!?$', lower):
            level = lower[0]
            suit = lower[1]
            has_alert = '!' in lower
            return Bid(level=level, suit=suit, has_alert=has_alert)
        elif lower == 'p':
            return Bid(is_pass=True)
        elif lower == 'x' or lower == 'd':
            return Bid(is_double=True)
        elif lower == 'xx':
            return Bid(is_redouble=True)
        raise Exception('Invalid bid: ' + value)

    def __eq__(self, other):
        return isinstance(other, Bid) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        if self.is_pass:
            return 'p'
        elif self.is_double:
            return 'x'
        elif self.is_redouble:
            return 'xx'
        contract = str(self.level) + self.suit
        if self.has_alert:
            contract = contract + '!'
        return contract
