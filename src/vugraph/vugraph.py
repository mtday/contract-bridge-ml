
"""
Provides the ability to parse the contents of a Vugraph `lin` file.
"""

from .vugraphah import VugraphAH
from .vugraphan import VugraphAN
from .vugraphmb import VugraphMB
from .vugraphmc import VugraphMC
from .vugraphmd import VugraphMD
from .vugraphnt import VugraphNT
from .vugraphpc import VugraphPC
from .vugraphpg import VugraphPG
from .vugraphpn import VugraphPN
from .vugraphqx import VugraphQX
from .vugraphrh import VugraphRH
from .vugraphrs import VugraphRS
from .vugraphst import VugraphST
from .vugraphsv import VugraphSV
from .vugraphvg import VugraphVG


class Vugraph(object):
    TYPES = {
        'ah': VugraphAH.parse,
        'an': VugraphAN.parse,
        'mb': VugraphMB.parse,
        'mc': VugraphMC.parse,
        'md': VugraphMD.parse,
        'nt': VugraphNT.parse,
        'pc': VugraphPC.parse,
        'pg': VugraphPG.parse,
        'pn': VugraphPN.parse,
        'qx': VugraphQX.parse,
        'rh': VugraphRH.parse,
        'rs': VugraphRS.parse,
        'st': VugraphST.parse,
        'sv': VugraphSV.parse,
        'vg': VugraphVG.parse
    }

    def __init__(self, content):
        self.content = content

    @staticmethod
    def parse(vugraph_data):
        content = []
        vugraph_lines = vugraph_data.split('\n')
        for line in vugraph_lines:
            parts = line.split('|')
            index = 0
            while index < len(parts) - 1:
                key = parts[index]
                value = parts[index + 1]
                if key in Vugraph.TYPES:
                    content.append(Vugraph.TYPES[key](value))
                index = index + 2
        return Vugraph(content)

    def __eq__(self, other):
        return isinstance(other, Vugraph) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        s = ''
        for item in self.content:
            s += str(item) + '\n'
        return s
