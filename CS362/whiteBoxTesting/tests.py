# Jhonatan Becerra
# HW#2 - Improving Coverage
# Before writing the tests, I figured out what the domain
# which would trigger each conditional was. This allowed me
# to target each instance easily and accurately.
# For the 'if' statement, the domain was [101-149]
# For the first 'elif', [1-47]
# For the second 'elif', [50 - 100, divisible by 5]

import unittest
from contrived_func import contrived_func


class WhiteBoxTest(unittest.TestCase):
    # trigger 'if' with a number between 100 and 150
    # which makes both conditions true
    def test_if_tt(self):
        self.assertTrue(contrived_func(101))

    # trigger first elif with 6
    def test_elif_tt(self):
        self.assertFalse(contrived_func(6))

    # trigger first elif with a number which meets both
    # conditions, but is not 6
    def test_elif_tt_not6(self):
        self.assertTrue(contrived_func(47))

    # target first elif with a number which met the
    # first constraint, but not the second. In effect,
    # it simply defaulted to the else part
    def test_elif_tf(self):
        self.assertFalse(contrived_func(48))

    # trigger the second elif with conditions which
    # were within the constraints of all 3 conditions
    def test_elif2_ttt(self):
        self.assertTrue(contrived_func(50))

    # trigger the second elif with the first part of the 'or'
    # being true, but not the second. The number is also divisible
    # by 5
    def test_elif2_tft(self):
        self.assertTrue(contrived_func(80))

    # default: number not in the range of any of the other
    # conditionals
    def test_else(self):
        self.assertFalse(contrived_func(361))


if __name__ == '__main__':
    unittest.main()