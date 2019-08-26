
from vugraph import VugraphQX
import unittest


class TestVugraphQX(unittest.TestCase):
    def test_init(self):
        self.assertEqual(VugraphQX('o', 1).hand_type, 'o')
        self.assertEqual(VugraphQX('o', 1).board_number, 1)
        self.assertEqual(VugraphQX('c', 33).hand_type, 'c')
        self.assertEqual(VugraphQX('c', 33).board_number, 33)

    def test_parse_hand_type(self):
        self.assertEqual(VugraphQX.parse('o1').hand_type, 'o')
        self.assertEqual(VugraphQX.parse('c33').hand_type, 'c')

    def test_parse_board_number(self):
        self.assertEqual(VugraphQX.parse('o1').board_number, 1)
        self.assertEqual(VugraphQX.parse('c33').board_number, 33)

    def test_parse_invalid(self):
        with self.assertRaises(Exception) as context:
            VugraphQX.parse('x1')  # x is not a valid hand type


if __name__ == '__main__':
    unittest.main()
