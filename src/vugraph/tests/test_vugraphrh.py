
from vugraph import VugraphRH
import unittest


class TestVugraphRH(unittest.TestCase):
    def test_init(self):
        VugraphRH()  # nothing really to test

    def test_parse(self):
        VugraphRH.parse('')  # nothing really to test

    def test_parse_invalid(self):
        pass  # nothing really to test


if __name__ == '__main__':
    unittest.main()
