from vugraph import VugraphMC
import unittest


class TestVugraphMC(unittest.TestCase):
    def test_init(self):
        self.assertEqual(VugraphMC(10).tricks_taken, 10)

    def test_parse(self):
        self.assertEqual(VugraphMC.parse('10').tricks_taken, 10)


if __name__ == '__main__':
    unittest.main()
