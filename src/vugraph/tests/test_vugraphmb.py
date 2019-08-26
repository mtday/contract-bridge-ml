from model import Bid
from vugraph import VugraphMB
import unittest


class TestVugraphMB(unittest.TestCase):
    def test_init(self):
        self.assertEqual(VugraphMB(Bid(is_pass=True)).bid, Bid(is_pass=True))

    def test_parse(self):
        self.assertEqual(VugraphMB.parse('3c').bid, Bid(level=3, suit='c'))
        self.assertEqual(VugraphMB.parse('p').bid, Bid(is_pass=True))
        self.assertEqual(VugraphMB.parse('x').bid, Bid(is_double=True))
        self.assertEqual(VugraphMB.parse('d').bid, Bid(is_double=True))
        self.assertEqual(VugraphMB.parse('xx').bid, Bid(is_redouble=True))


if __name__ == '__main__':
    unittest.main()
