
from vugraph import VugraphAN
import unittest


class TestVugraphAN(unittest.TestCase):
    def test_init(self):
        self.assertEqual(VugraphAN('annotation').annotation, 'annotation')

    def test_parse(self):
        self.assertEqual(VugraphAN.parse('annotation').annotation, 'annotation')


if __name__ == '__main__':
    unittest.main()
