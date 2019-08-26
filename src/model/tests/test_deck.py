
from model import Card
from model import Deck
import unittest


class TestDeck(unittest.TestCase):
    def test_cards(self):
        cards = Deck.cards()
        self.assertEqual(len(cards), 52)
        self.assertEqual(Card('c', '2'), cards[0])
        self.assertEqual(Card('s', 'a'), cards[-1])


if __name__ == '__main__':
    unittest.main()
