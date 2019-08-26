
from pathlib import Path
from vugraph import Vugraph
from vugraph import VugraphRS
from vugraph import VugraphVG
import unittest


class TestVugraph(unittest.TestCase):
    def test_init(self):
        content = [
            VugraphVG.parse('Schapiro Spring 4s,Final - EXTRA TIME,I,1,40,Liggins,47,Wolfarth,49'),
            VugraphRS.parse('2HN+2,4HN=,4SS=,4SS=,2SS=,3DE-2,4SN+1,4SN+2,4SE-1,2SW+3,4SS+1,6SNx-1,4SS-1,3SN=')
        ]
        vugraph = Vugraph(content)
        self.assertEqual(vugraph.content, content)

    def test_parse(self):
        with Path(__file__).parent.joinpath('test_vugraph.lin').open() as file:
            vugraph = Vugraph.parse(file.read())
            content = vugraph.content
            self.assertEqual(len(content), 1601)


if __name__ == '__main__':
    unittest.main()
