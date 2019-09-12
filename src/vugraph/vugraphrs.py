
from model import Result

"""
Provides a comma-delimited list of the results of each board. For example:

1nw+3,1nw+3,5de=,5dw+1,2ns=,3cs-1,4sw=,4sw=
,,,,1nw+3,1nw+3,5de=,5dw+1,2ns=,3cs-1,4sw=,4sw=
"""


class VugraphRS(object):
    def __init__(self, results):
        self.results = results

    @staticmethod
    def parse(rs):
        results_list = rs.split(',')
        results = {}
        index = 0
        while index < len(results_list):
            result_str = results_list[index]
            if '' != result_str:
                result = Result.parse(result_str)
                deal = index // 2
                if deal not in results:
                    results[deal] = []
                results[deal].append(result)
            index += 1
        return VugraphRS(results)

