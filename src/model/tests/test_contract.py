
from model import Contract
import unittest


class TestContract(unittest.TestCase):
    def test_init_level(self):
        self.assertEqual(Contract('1', 'c', 'n').level, '1')
        self.assertEqual(Contract('2', 'd', 's').level, '2')
        self.assertEqual(Contract('3', 'n', 'e').level, '3')
        self.assertEqual(Contract('4', 'h', 'w').level, '4')
        self.assertEqual(Contract('5', 's', 'n', True).level, '5')
        self.assertIsNone(Contract(passout=True).level)

    def test_init_suit(self):
        self.assertEqual(Contract('1', 'c', 'n').suit, 'c')
        self.assertEqual(Contract('2', 'd', 's').suit, 'd')
        self.assertEqual(Contract('3', 'n', 'e').suit, 'n')
        self.assertEqual(Contract('4', 'h', 'w').suit, 'h')
        self.assertEqual(Contract('5', 's', 'n', True).suit, 's')
        self.assertIsNone(Contract(passout=True).suit)

    def test_init_declarer(self):
        self.assertEqual(Contract('1', 'c', 'n').declarer, 'n')
        self.assertEqual(Contract('2', 'd', 's').declarer, 's')
        self.assertEqual(Contract('3', 'n', 'e').declarer, 'e')
        self.assertEqual(Contract('4', 'h', 'w').declarer, 'w')
        self.assertEqual(Contract('5', 's', 'n', True).declarer, 'n')
        self.assertIsNone(Contract(passout=True).declarer)

    def test_init_doubled(self):
        self.assertFalse(Contract('1', 'c', 'n').doubled)
        self.assertTrue(Contract('5', 's', 'n', True).doubled)
        self.assertFalse(Contract('5', 's', 'n', False, True).doubled)
        self.assertFalse(Contract(passout=True).doubled)

    def test_init_redoubled(self):
        self.assertFalse(Contract('1', 'c', 'n').redoubled)
        self.assertFalse(Contract('5', 's', 'n', True).redoubled)
        self.assertFalse(Contract('5', 's', 'n', False, False).redoubled)
        self.assertTrue(Contract('5', 's', 'n', False, True).redoubled)
        self.assertFalse(Contract(passout=True).redoubled)

    def test_init_passout(self):
        self.assertFalse(Contract('1', 'c', 'n').passout)
        self.assertFalse(Contract('5', 's', 'n', True).passout)
        self.assertFalse(Contract('5', 's', 'n', False, False).passout)
        self.assertFalse(Contract('5', 's', 'n', False, True).passout)
        self.assertTrue(Contract(passout=True).passout)

    def test_parse_valid(self):
        self.assertEqual(str(Contract.parse('1cn')), '1cn')
        self.assertEqual(str(Contract.parse('2ds')), '2ds')
        self.assertEqual(str(Contract.parse('3ne')), '3ne')
        self.assertEqual(str(Contract.parse('4hw')), '4hw')
        self.assertEqual(str(Contract.parse('5snx')), '5snx')
        self.assertEqual(str(Contract.parse('6csxx')), '6csxx')
        self.assertEqual(str(Contract.parse('1CN')), '1cn')
        self.assertEqual(str(Contract.parse('2DS')), '2ds')
        self.assertEqual(str(Contract.parse('3NE')), '3ne')
        self.assertEqual(str(Contract.parse('4HW')), '4hw')
        self.assertEqual(str(Contract.parse('5SNX')), '5snx')
        self.assertEqual(str(Contract.parse('6CSXX')), '6csxx')

    def test_parse_invalid(self):
        with self.assertRaises(Exception) as context:
            Contract.parse('8cn')  # 8 not a valid level
        with self.assertRaises(Exception) as context:
            Contract.parse('1xs')  # x not a valid suit
        with self.assertRaises(Exception) as context:
            Contract.parse('1cx')  # x not a valid declarer

    def test_repr(self):
        self.assertEqual(str(Contract.parse('1cn')), '1cn')
        self.assertEqual(str(Contract.parse('2ds')), '2ds')
        self.assertEqual(str(Contract.parse('3ne')), '3ne')
        self.assertEqual(str(Contract.parse('4hw')), '4hw')
        self.assertEqual(str(Contract.parse('5snx')), '5snx')
        self.assertEqual(str(Contract.parse('6csxx')), '6csxx')


if __name__ == '__main__':
    unittest.main()
