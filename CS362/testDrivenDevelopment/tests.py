# Jhonatan Becerra
# tests.py check for a valid password

import unittest
from check_pwd import check_pwd


class TestLength(unittest.TestCase):
    # empty string
    def test_empty(self):
        self.assertFalse(check_pwd(""))

    # over 21 character
    def test_21chars(self):
        self.assertFalse(check_pwd("abcdefghijklmnopqrstuv"))

class TestStringCase(unittest.TestCase):
    # check for presence of lowercase
    def test_lowercase(self):
        self.assertFalse(check_pwd("THISISATEST"))

    # check for presence of uppercase
    def test_uppercase(self):
        self.assertFalse(check_pwd("thisisatest"))

class TestStringSpecialChars(unittest.TestCase):
    # check for digits
    def test_digit(self):
        self.assertFalse(check_pwd("thisIsATest"))

    # check for symbols
    def test_symbol(self):
        self.assertFalse(check_pwd("thisIsATest11"))


if __name__ == "__main__":
    unittest.main()