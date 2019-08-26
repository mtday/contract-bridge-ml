from model import Hand
from vugraph import VugraphMD
import unittest


class TestVugraphMD(unittest.TestCase):
    def test_init(self):
        hands = [
            Hand.parse('SQJHQT9632D82CK98'),
            Hand.parse('S8743HK854DK76CQ2'),
            Hand.parse('SAT2HAJ7DAJ543CJ5'),
            Hand.parse('SK965HDQT9CAT7643')
        ]
        md = VugraphMD(3, hands)
        self.assertEqual(md.dealer, 3)
        self.assertEqual(md.hands, hands)

    def test_parse_none_missing(self):
        md = VugraphMD.parse('3SQJHQT9632D82CK98,S8743HK854DK76CQ2,SAT2HAJ7DAJ543CJ5,SK965HDQT9CAT7643')
        self.assertEqual(md.dealer, 3)
        self.assertEqual(len(md.hands), 4)
        self.assertEqual(md.hands[0], Hand.parse('SQJHQT9632D82CK98'))
        self.assertEqual(md.hands[1], Hand.parse('S8743HK854DK76CQ2'))
        self.assertEqual(md.hands[2], Hand.parse('SAT2HAJ7DAJ543CJ5'))
        self.assertEqual(md.hands[3], Hand.parse('SK965HDQT9CAT7643'))

    def test_parse_with_gaps(self):
        md = VugraphMD.parse('3SQH269D347QKC34QK,S68KAH37QD2JAC27A,S2357H8JAD568C69J,')
        self.assertEqual(md.dealer, 3)
        self.assertEqual(len(md.hands), 4)
        self.assertEqual(md.hands[0], Hand.parse('SQH269D347QKC34QK'))
        self.assertEqual(md.hands[1], Hand.parse('S68KAH37QD2JAC27A'))
        self.assertEqual(md.hands[2], Hand.parse('S2357H8JAD568C69J'))
        self.assertEqual(md.hands[3], Hand.parse('s49tjh45tkd9tc58t'))


if __name__ == '__main__':
    unittest.main()
