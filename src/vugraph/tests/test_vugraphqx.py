
from vugraph import VugraphQX
import unittest


class TestVugraphQX(unittest.TestCase):
    def test_init(self):
        self.assertEqual(VugraphQX('o', 1).room, 'o')
        self.assertEqual(VugraphQX('o', 1).board_number, 1)
        self.assertEqual(VugraphQX('c', 33).room, 'c')
        self.assertEqual(VugraphQX('c', 33).board_number, 33)

    def test_parse_room(self):
        self.assertEqual(VugraphQX.parse('o1').room, 'o')
        self.assertEqual(VugraphQX.parse('c33').room, 'c')

    def test_parse_board_number(self):
        self.assertEqual(VugraphQX.parse('o1').board_number, 1)
        self.assertEqual(VugraphQX.parse('c33').board_number, 33)

    def test_parse_invalid(self):
        with self.assertRaises(Exception):
            VugraphQX.parse('x1')  # x is not a valid hand type


if __name__ == '__main__':
    unittest.main()
