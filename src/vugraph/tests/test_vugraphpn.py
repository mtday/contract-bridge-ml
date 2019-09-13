
from vugraph import VugraphPN
import unittest


class TestVugraphPN(unittest.TestCase):
    def test_init(self):
        names = ['Name1', 'Name2', 'Name3', 'Name4']
        pn = VugraphPN(names)
        self.assertEqual(pn.names, names)

    def test_parse(self):
        pn = VugraphPN.parse('Name1,Name2,Name3,Name4')
        self.assertEqual(len(pn.names), 4)
        self.assertEqual(pn.names[0], 'Name1')
        self.assertEqual(pn.names[1], 'Name2')
        self.assertEqual(pn.names[2], 'Name3')
        self.assertEqual(pn.names[3], 'Name4')

    def test_parse_invalid(self):
        with self.assertRaises(Exception):
            VugraphPN.parse('Name1,Name2')  # number of names needs to be a multiple of 4


if __name__ == '__main__':
    unittest.main()
