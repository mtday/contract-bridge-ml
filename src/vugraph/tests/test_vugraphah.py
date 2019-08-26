
from vugraph import VugraphAH
import unittest


class TestVugraphAH(unittest.TestCase):
    def test_init(self):
        self.assertEqual(VugraphAH('description').description, 'description')

    def test_parse(self):
        self.assertEqual(VugraphAH.parse('description').description, 'description')


if __name__ == '__main__':
    unittest.main()
