
from vugraph import VugraphSV
import unittest


class TestVugraphSV(unittest.TestCase):
    def test_init(self):
        self.assertEqual(VugraphSV('b').board_type, 'b')
        self.assertEqual(VugraphSV('e').board_type, 'e')
        self.assertEqual(VugraphSV('n').board_type, 'n')
        self.assertEqual(VugraphSV('o').board_type, 'o')

    def test_parse(self):
        self.assertEqual(VugraphSV.parse('b').board_type, 'b')
        self.assertEqual(VugraphSV.parse('e').board_type, 'e')
        self.assertEqual(VugraphSV.parse('n').board_type, 'n')
        self.assertEqual(VugraphSV.parse('o').board_type, 'o')


if __name__ == '__main__':
    unittest.main()
