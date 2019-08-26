
from model import Card
from model import Hand
import unittest


class TestHand(unittest.TestCase):
    def test_init(self):
        cards = [
            Card('s', '7'),
            Card('s', '6'),
            Card('s', '4'),
            Card('s', '3'),
            Card('h', 'a'),
            Card('h', 'k'),
            Card('h', 't'),
            Card('d', 'q'),
            Card('d', 'j'),
            Card('d', '8'),
            Card('c', 't'),
            Card('c', '5'),
            Card('c', '2')
        ]
        hand = Hand(cards)
        self.assertEqual(len(hand.cards), 13)
        # cards are re-ordered from lowest to highest
        self.assertEqual(hand.cards[0], Card('c', '2'))
        self.assertEqual(hand.cards[-1], Card('s', '7'))
        # cards are sorted into suits in the dict
        self.assertEqual(len(hand.card_dict['c']), 3)
        self.assertEqual(Card('c', '2'), hand.card_dict['c'][0])
        self.assertEqual(Card('c', '5'), hand.card_dict['c'][1])
        self.assertEqual(Card('c', 't'), hand.card_dict['c'][2])
        self.assertEqual(len(hand.card_dict['d']), 3)
        self.assertEqual(Card('d', '8'), hand.card_dict['d'][0])
        self.assertEqual(Card('d', 'j'), hand.card_dict['d'][1])
        self.assertEqual(Card('d', 'q'), hand.card_dict['d'][2])
        self.assertEqual(len(hand.card_dict['h']), 3)
        self.assertEqual(Card('h', 't'), hand.card_dict['h'][0])
        self.assertEqual(Card('h', 'k'), hand.card_dict['h'][1])
        self.assertEqual(Card('h', 'a'), hand.card_dict['h'][2])
        self.assertEqual(len(hand.card_dict['s']), 4)
        self.assertEqual(Card('s', '3'), hand.card_dict['s'][0])
        self.assertEqual(Card('s', '4'), hand.card_dict['s'][1])
        self.assertEqual(Card('s', '6'), hand.card_dict['s'][2])
        self.assertEqual(Card('s', '7'), hand.card_dict['s'][3])

    def test_parse_valid(self):
        self.assertEqual(str(Hand.parse('sakqjt98765432')), 's23456789tjqka')
        self.assertEqual(str(Hand.parse('s23456789tjqka')), 's23456789tjqka')
        self.assertEqual(str(Hand.parse('sqh269d347qkc34qk')), 'c34qkd347qkh269sq')
        self.assertEqual(str(Hand.parse('SAKQJT98765432')), 's23456789tjqka')
        self.assertEqual(str(Hand.parse('SQH269D347QKC34QK')), 'c34qkd347qkh269sq')
        self.assertEqual(str(Hand.parse('saskhqhjdtd9d8c7c6c5s4s3h2')), 'c567d89th2jqs34ka')

    def test_init_invalid(self):
        with self.assertRaises(Exception) as context:
            Hand('akqjt98765432')  # missing suit
        with self.assertRaises(Exception) as context:
            Hand('sakqjt98765432a')  # too many cards
        with self.assertRaises(Exception) as context:
            Hand('sakqjt987d765432')  # too many cards


if __name__ == '__main__':
    unittest.main()
