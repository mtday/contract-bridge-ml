
from vugraph import VugraphST
import unittest


class TestVugraphST(unittest.TestCase):
    def test_init(self):
        VugraphST()  # nothing really to test

    def test_parse(self):
        VugraphST.parse('')  # nothing really to test

    def test_parse_invalid(self):
        pass  # nothing really to test


if __name__ == '__main__':
    unittest.main()
