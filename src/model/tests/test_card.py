
from model import Card
import unittest


class TestCard(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Card('c', '2').suit, 'c')
        self.assertEqual(Card('c', '2').level, '2')

    def test_parse_valid(self):
        self.assertEqual(Card.parse('c2').suit, 'c')
        self.assertEqual(Card.parse('c2').level, '2')
        self.assertEqual(Card.parse('C2').suit, 'c')
        self.assertEqual(Card.parse('C2').level, '2')

    def test_parse_invalid(self):
        with self.assertRaises(Exception) as context:
            Card.parse('x2')  # x not a valid suit
        with self.assertRaises(Exception) as context:
            Card.parse('c1')  # 1 not a valid level

    def test_order(self):
        self.assertEqual(Card.parse('c2').order(), 0)
        self.assertEqual(Card.parse('d9').order(), 20)
        self.assertEqual(Card.parse('ht').order(), 34)
        self.assertEqual(Card.parse('sa').order(), 51)

    def test_repr(self):
        self.assertEqual(str(Card.parse('c2')), 'c2')


if __name__ == '__main__':
    unittest.main()
