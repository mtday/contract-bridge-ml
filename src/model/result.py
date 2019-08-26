
from .contract import Contract

import re


class Result(object):
    def __init__(self, contract, result):
        self.contract = contract
        self.result = result

    @staticmethod
    def parse(value):
        lower = value.lower()
        if not re.match('^[1-7][cdhsn][nsew]x{0,2}((=)|([+-][1-7]))$', lower):
            raise Exception('Invalid result: ' + value)
        contract = Contract.parse(re.findall('^[1-7][cdhsn][nsew]x{0,2}', lower)[0])
        if '=' in lower:
            result = 0
        elif '+' in lower:
            result = int(lower[-1])
        else:
            result = -int(lower[-1])
        return Result(contract, result)

    def __eq__(self, other):
        return isinstance(other, Result) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        rep = str(self.contract)
        if self.result == 0:
            rep = rep + '='
        elif self.result > 0:
            rep = rep + '+' + str(self.result)
        else:
            rep = rep + str(self.result)
        return rep
