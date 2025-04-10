import unittest
from year import is_leap_year

class TestLeapYear(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2004))
        self.assertTrue(is_leap_year(2024))

    def test_false_cases(self):
        self.assertFalse(is_leap_year(1990))
        self.assertFalse(is_leap_year(2001))
        self.assertFalse(is_leap_year(2025))
 
if __name__ == '__main__':
    unittest.main()