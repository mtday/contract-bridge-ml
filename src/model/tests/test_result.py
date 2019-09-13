
from model import Contract
from model import Result
import unittest


class TestResult(unittest.TestCase):
    def test_init_contract(self):
        self.assertEqual(Result(Contract.parse('1cn'), 0).contract, Contract.parse('1cn'))
        self.assertEqual(Result(Contract.parse('2ds'), -1).contract, Contract.parse('2ds'))
        self.assertEqual(Result(Contract.parse('3ne'), 1).contract, Contract.parse('3ne'))
        self.assertEqual(Result(Contract.parse('4hw'), -2).contract, Contract.parse('4hw'))
        self.assertEqual(Result(Contract.parse('5snx'), 2).contract, Contract.parse('5snx'))
        self.assertEqual(Result(Contract.parse('6csxx'), 0).contract, Contract.parse('6csxx'))

    def test_init_result(self):
        self.assertEqual(Result(Contract.parse('1cn'), 0).result, 0)
        self.assertEqual(Result(Contract.parse('2ds'), -1).result, -1)
        self.assertEqual(Result(Contract.parse('3ne'), 1).result, 1)
        self.assertEqual(Result(Contract.parse('4hw'), -2).result, -2)
        self.assertEqual(Result(Contract.parse('5snx'), 2).result, 2)

    def test_parse_valid(self):
        self.assertEqual(str(Result.parse('1cn=')), '1cn=')
        self.assertEqual(str(Result.parse('2ds-1')), '2ds-1')
        self.assertEqual(str(Result.parse('3ne+1')), '3ne+1')
        self.assertEqual(str(Result.parse('4hw-2')), '4hw-2')
        self.assertEqual(str(Result.parse('5snx+2')), '5snx+2')
        self.assertEqual(str(Result.parse('6csxx=')), '6csxx=')
        self.assertEqual(str(Result.parse('1CN=')), '1cn=')
        self.assertEqual(str(Result.parse('2DS-1')), '2ds-1')
        self.assertEqual(str(Result.parse('3NE+1')), '3ne+1')
        self.assertEqual(str(Result.parse('4HW-2')), '4hw-2')
        self.assertEqual(str(Result.parse('5SNX+2')), '5snx+2')
        self.assertEqual(str(Result.parse('6CSXX=')), '6csxx=')

    def test_parse_invalid(self):
        with self.assertRaises(Exception):
            Result.parse('8cn=')  # 8 not a valid level
        with self.assertRaises(Exception):
            Result.parse('1xs=')  # x not a valid suit
        with self.assertRaises(Exception):
            Result.parse('1cx=')  # x not a valid declarer
        with self.assertRaises(Exception):
            Result.parse('1cn')  # missing score
        with self.assertRaises(Exception):
            Result.parse('1cn=0')  # unexpected trailing 0
        with self.assertRaises(Exception):
            Result.parse('1cn-8')  # -8 not valid result
        with self.assertRaises(Exception):
            Result.parse('1cn+8')  # +8 not valid result

    def test_repr(self):
        self.assertEqual(str(Result.parse('1cn=')), '1cn=')
        self.assertEqual(str(Result.parse('2ds-1')), '2ds-1')
        self.assertEqual(str(Result.parse('3ne+1')), '3ne+1')
        self.assertEqual(str(Result.parse('4hw-2')), '4hw-2')
        self.assertEqual(str(Result.parse('5snx+2')), '5snx+2')
        self.assertEqual(str(Result.parse('6csxx=')), '6csxx=')


if __name__ == '__main__':
    unittest.main()
