from model import Result
from vugraph import VugraphRS
from vugraph import VugraphVG
import unittest


class TestVugraphRS(unittest.TestCase):
    def test_init(self):
        results = {
            1: [Result.parse('1nn='), Result.parse('1nn+1')],
            2: [Result.parse('4ss='), Result.parse('4ss-1')]
        }
        rs = VugraphRS(results)
        self.assertEqual(rs.results, results)

    def test_parse_none_missing(self):
        rs = VugraphRS.parse('1nw+3,1nw+3,5de=,5dw+1,2ns=,3cs-1,4sw=,4sw=')
        self.assertEqual(rs.results[0][0], Result.parse('1nw+3'))
        self.assertEqual(rs.results[0][1], Result.parse('1nw+3'))
        self.assertEqual(rs.results[1][0], Result.parse('5de='))
        self.assertEqual(rs.results[1][1], Result.parse('5dw+1'))
        self.assertEqual(rs.results[2][0], Result.parse('2ns='))
        self.assertEqual(rs.results[2][1], Result.parse('3cs-1'))
        self.assertEqual(rs.results[3][0], Result.parse('4sw='))
        self.assertEqual(rs.results[3][1], Result.parse('4sw='))

    def test_parse_with_gaps(self):
        rs = VugraphRS.parse(',,,,1nw+3,1nw+3,5de=,5dw+1,2ns=,3cs-1,4sw=,4sw=')
        self.assertFalse(0 in rs.results)
        self.assertFalse(1 in rs.results)
        self.assertEqual(rs.results[2][0], Result.parse('1nw+3'))
        self.assertEqual(rs.results[2][1], Result.parse('1nw+3'))
        self.assertEqual(rs.results[3][0], Result.parse('5de='))
        self.assertEqual(rs.results[3][1], Result.parse('5dw+1'))
        self.assertEqual(rs.results[4][0], Result.parse('2ns='))
        self.assertEqual(rs.results[4][1], Result.parse('3cs-1'))
        self.assertEqual(rs.results[5][0], Result.parse('4sw='))
        self.assertEqual(rs.results[5][1], Result.parse('4sw='))


if __name__ == '__main__':
    unittest.main()
