from model import Card
from vugraph import VugraphPC
import unittest


class TestVugraphPC(unittest.TestCase):
    def test_init(self):
        self.assertEqual(VugraphPC(Card('c', '2')).card, Card('c', '2'))

    def test_parse(self):
        self.assertEqual(VugraphPC.parse('c2').card, Card('c', '2'))


if __name__ == '__main__':
    unittest.main()
