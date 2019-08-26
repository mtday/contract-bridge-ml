
from vugraph import VugraphVG
import unittest


class TestVugraphVG(unittest.TestCase):
    def test_init(self):
        vg = VugraphVG('description', 'note', 'I', 1, 14, 'USA', 0, 'France', 0)
        self.assertEqual(vg.description, 'description')
        self.assertEqual(vg.note, 'note')
        self.assertEqual(vg.round_type, 'I')
        self.assertEqual(vg.start_deal, 1)
        self.assertEqual(vg.end_deal, 14)
        self.assertEqual(vg.team1, 'USA')
        self.assertEqual(vg.team1_points, 0)
        self.assertEqual(vg.team2, 'France')
        self.assertEqual(vg.team2_points, 0)

    def test_parse(self):
        vg = VugraphVG.parse('WBF Youth World Online Team Championships,Final 4/4,I,1,14,USA,0,France,0')
        self.assertEqual(vg.description, 'WBF Youth World Online Team Championships')
        self.assertEqual(vg.note, 'Final 4/4')
        self.assertEqual(vg.round_type, 'I')
        self.assertEqual(vg.start_deal, 1)
        self.assertEqual(vg.end_deal, 14)
        self.assertEqual(vg.team1, 'USA')
        self.assertEqual(vg.team1_points, 0)
        self.assertEqual(vg.team2, 'France')
        self.assertEqual(vg.team2_points, 0)


if __name__ == '__main__':
    unittest.main()
