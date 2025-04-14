import unittest
from year import is_leap_year

class TestLeapYear(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(is_leap_year(2000)) #is a leap year 
        self.assertTrue(is_leap_year(2004)) #is a leap year 
        self.assertTrue(is_leap_year(2024)) #is a leap year 

    def test_false_cases(self):
        self.assertFalse(is_leap_year(1990)) #is not a leap year 
        self.assertFalse(is_leap_year(2001)) #is not a leap year 
        self.assertFalse(is_leap_year(2025)) #is not a leap year 
 
if __name__ == '__main__':
    unittest.main()