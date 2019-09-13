
from model import Bid
import unittest


class TestBid(unittest.TestCase):
    def test_init_level(self):
        self.assertEqual(Bid(level='1', suit='c').level, '1')
        self.assertEqual(Bid(level='2', suit='d').level, '2')
        self.assertEqual(Bid(level='3', suit='n').level, '3')
        self.assertEqual(Bid(level='4', suit='h').level, '4')
        self.assertEqual(Bid(level='5', suit='s').level, '5')
        self.assertEqual(Bid(level='5', suit='s', has_alert=True).level, '5')
        self.assertEqual(Bid(level='5', suit='s', has_alert=True, annotation='Alert').level, '5')
        self.assertIsNone(Bid(is_pass=True).level)
        self.assertIsNone(Bid(is_double=True).level)
        self.assertIsNone(Bid(is_redouble=True).level)

    def test_init_suit(self):
        self.assertEqual(Bid(level='1', suit='c').suit, 'c')
        self.assertEqual(Bid(level='2', suit='d').suit, 'd')
        self.assertEqual(Bid(level='3', suit='n').suit, 'n')
        self.assertEqual(Bid(level='4', suit='h').suit, 'h')
        self.assertEqual(Bid(level='5', suit='s').suit, 's')
        self.assertEqual(Bid(level='5', suit='s', has_alert=True).suit, 's')
        self.assertEqual(Bid(level='5', suit='s', has_alert=True, annotation='Alert').suit, 's')
        self.assertIsNone(Bid(is_pass=True).suit)
        self.assertIsNone(Bid(is_double=True).suit)
        self.assertIsNone(Bid(is_redouble=True).suit)

    def test_init_contract(self):
        self.assertTrue(Bid(level='1', suit='c').is_contract)
        self.assertTrue(Bid(level='2', suit='d').is_contract)
        self.assertTrue(Bid(level='3', suit='n').is_contract)
        self.assertTrue(Bid(level='4', suit='h').is_contract)
        self.assertTrue(Bid(level='5', suit='s').is_contract)
        self.assertTrue(Bid(level='5', suit='s', has_alert=True).is_contract)
        self.assertTrue(Bid(level='5', suit='s', has_alert=True, annotation='Alert').is_contract)
        self.assertFalse(Bid(is_pass=True).is_contract)
        self.assertFalse(Bid(is_double=True).is_contract)
        self.assertFalse(Bid(is_redouble=True).is_contract)

    def test_init_pass(self):
        self.assertFalse(Bid(level='1', suit='c').is_pass)
        self.assertFalse(Bid(level='2', suit='d').is_pass)
        self.assertFalse(Bid(level='3', suit='n').is_pass)
        self.assertFalse(Bid(level='4', suit='h').is_pass)
        self.assertFalse(Bid(level='5', suit='s').is_pass)
        self.assertFalse(Bid(level='5', suit='s', has_alert=True).is_pass)
        self.assertFalse(Bid(level='5', suit='s', has_alert=True, annotation='Alert').is_pass)
        self.assertTrue(Bid(is_pass=True).is_pass)
        self.assertFalse(Bid(is_double=True).is_pass)
        self.assertFalse(Bid(is_redouble=True).is_pass)

    def test_init_double(self):
        self.assertFalse(Bid(level='1', suit='c').is_double)
        self.assertFalse(Bid(level='2', suit='d').is_double)
        self.assertFalse(Bid(level='3', suit='n').is_double)
        self.assertFalse(Bid(level='4', suit='h').is_double)
        self.assertFalse(Bid(level='5', suit='s').is_double)
        self.assertFalse(Bid(level='5', suit='s', has_alert=True).is_double)
        self.assertFalse(Bid(level='5', suit='s', has_alert=True, annotation='Alert').is_double)
        self.assertFalse(Bid(is_pass=True).is_double)
        self.assertTrue(Bid(is_double=True).is_double)
        self.assertFalse(Bid(is_redouble=True).is_double)

    def test_init_redouble(self):
        self.assertFalse(Bid(level='1', suit='c').is_redouble)
        self.assertFalse(Bid(level='2', suit='d').is_redouble)
        self.assertFalse(Bid(level='3', suit='n').is_redouble)
        self.assertFalse(Bid(level='4', suit='h').is_redouble)
        self.assertFalse(Bid(level='5', suit='s').is_redouble)
        self.assertFalse(Bid(level='5', suit='s', has_alert=True).is_redouble)
        self.assertFalse(Bid(level='5', suit='s', has_alert=True, annotation='Alert').is_redouble)
        self.assertFalse(Bid(is_pass=True).is_redouble)
        self.assertFalse(Bid(is_double=True).is_redouble)
        self.assertTrue(Bid(is_redouble=True).is_redouble)

    def test_init_has_alert(self):
        self.assertFalse(Bid(level='1', suit='c').has_alert)
        self.assertFalse(Bid(level='2', suit='d').has_alert)
        self.assertFalse(Bid(level='3', suit='n').has_alert)
        self.assertFalse(Bid(level='4', suit='h').has_alert)
        self.assertFalse(Bid(level='5', suit='s').has_alert)
        self.assertTrue(Bid(level='5', suit='s', has_alert=True).has_alert)
        self.assertTrue(Bid(level='5', suit='s', has_alert=True, annotation='Alert').has_alert)
        self.assertFalse(Bid(is_pass=True).has_alert)
        self.assertFalse(Bid(is_double=True).has_alert)
        self.assertFalse(Bid(is_redouble=True).has_alert)

    def test_init_annotation(self):
        self.assertIsNone(Bid(level='1', suit='c').annotation)
        self.assertIsNone(Bid(level='2', suit='d').annotation)
        self.assertIsNone(Bid(level='3', suit='n').annotation)
        self.assertIsNone(Bid(level='4', suit='h').annotation)
        self.assertIsNone(Bid(level='5', suit='s').annotation)
        self.assertIsNone(Bid(level='5', suit='s', has_alert=True).annotation)
        self.assertEqual(Bid(level='5', suit='s', has_alert=True, annotation='Alert').annotation, 'Alert')
        self.assertIsNone(Bid(is_pass=True).annotation)
        self.assertIsNone(Bid(is_double=True).annotation)
        self.assertIsNone(Bid(is_redouble=True).annotation)

    def test_parse_valid(self):
        self.assertEqual(str(Bid.parse('1c')), '1c')
        self.assertEqual(str(Bid.parse('2d')), '2d')
        self.assertEqual(str(Bid.parse('3n')), '3n')
        self.assertEqual(str(Bid.parse('4h')), '4h')
        self.assertEqual(str(Bid.parse('5s!')), '5s!')
        self.assertEqual(str(Bid.parse('p')), 'p')
        self.assertEqual(str(Bid.parse('x')), 'x')
        self.assertEqual(str(Bid.parse('xx')), 'xx')
        self.assertEqual(str(Bid.parse('1C')), '1c')
        self.assertEqual(str(Bid.parse('2D')), '2d')
        self.assertEqual(str(Bid.parse('3N')), '3n')
        self.assertEqual(str(Bid.parse('4H')), '4h')
        self.assertEqual(str(Bid.parse('5S!')), '5s!')
        self.assertEqual(str(Bid.parse('P')), 'p')
        self.assertEqual(str(Bid.parse('X')), 'x')
        self.assertEqual(str(Bid.parse('XX')), 'xx')

    def test_parse_invalid(self):
        with self.assertRaises(Exception):
            Bid.parse('8c')  # 8 not a valid level
        with self.assertRaises(Exception):
            Bid.parse('1x')  # x not a valid suit

    def test_repr(self):
        self.assertEqual(str(Bid.parse('2d')), '2d')


if __name__ == '__main__':
    unittest.main()
