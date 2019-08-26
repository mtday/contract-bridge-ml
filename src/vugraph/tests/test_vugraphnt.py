
from vugraph import VugraphNT
import unittest


class TestVugraphNT(unittest.TestCase):
    def test_init(self):
        self.assertEqual(VugraphNT('note').note, 'note')

    def test_parse(self):
        self.assertEqual(VugraphNT.parse('note').note, 'note')


if __name__ == '__main__':
    unittest.main()
