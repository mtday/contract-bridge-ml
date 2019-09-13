
from vugraph import VugraphSV
import unittest


class TestVugraphSV(unittest.TestCase):
    def test_init(self):
        self.assertEqual(VugraphSV('b').vulnerability, 'b')
        self.assertEqual(VugraphSV('e').vulnerability, 'e')
        self.assertEqual(VugraphSV('n').vulnerability, 'n')
        self.assertEqual(VugraphSV('o').vulnerability, 'o')

    def test_parse(self):
        self.assertEqual(VugraphSV.parse('b').vulnerability, 'b')
        self.assertEqual(VugraphSV.parse('e').vulnerability, 'e')
        self.assertEqual(VugraphSV.parse('n').vulnerability, 'n')
        self.assertEqual(VugraphSV.parse('o').vulnerability, 'o')


if __name__ == '__main__':
    unittest.main()
