
from model import Deck
from model import Hand

"""
Defines the cards provided in each hand. May only specify 3 hands with the 4th being derived. The first digit
is assumed to be the hand that is the dealer. For example:

3SQH269D347QKC34QK,S68KAH37QD2JAC27A,S2357H8JAD568C69J,
3SQJHQT9632D82CK98,S8743HK854DK76CQ2,SAT2HAJ7DAJ543CJ5,SK965HDQT9CAT7643
"""


class VugraphMD(object):
    def __init__(self, dealer, hands):
        self.dealer = dealer
        self.hands = hands

    @staticmethod
    def parse(md):
        dealer = int(md[0:1])
        if dealer < 1 or dealer > 4:
            raise Exception('Unexpected dealer: ' + md)
        hands = []
        remaining_cards = Deck.cards()
        for hand_str in md[1:].split(','):
            if '' == hand_str:
                hands.append(Hand(remaining_cards))
            else:
                hand = Hand.parse(hand_str)
                hands.append(hand)
                for card in hand.cards:
                    remaining_cards.remove(card)
        if len(hands) != 4:
            raise Exception('Unexpected number of hands: ' + md)
        return VugraphMD(dealer, hands)
