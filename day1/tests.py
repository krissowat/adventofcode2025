import unittest
from day1 import part_2

class TestDay1(unittest.TestCase):
    # Copied from https://github.com/joltdx/advent-of-code-2025/blob/main/day01/src/tests.rs
    def test_1(self):
        self.assertEqual(part_2(['R49', 'L98']), 0)

    def test_2(self):
        self.assertEqual(part_2(['R49', 'R1']), 1)

    def test_3(self):
        self.assertEqual(part_2(['R49', 'R1', 'R1']), 1)

    def test_4(self):
        self.assertEqual(part_2(['R49', 'R1', 'L1']), 1)

    def test_5(self):
        self.assertEqual(part_2(['L50', 'L100']), 2)

    def test_6(self):
        self.assertEqual(part_2(['R50', 'R100']), 2)

    def test_7(self):
        self.assertEqual(part_2(['L50', 'L400']), 5)

    def test_8(self):
        self.assertEqual(part_2(['L50', 'R400']), 5)

    def test_9(self):
        self.assertEqual(part_2(['R1000']), 10)



if __name__ == '__main__':
    unittest.main()