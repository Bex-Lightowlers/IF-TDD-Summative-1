import unittest
from year import is_leap_year

def is_leap_year(year):
    return (year % 4 ==0 and year % 100 !=0) or (year % 400 ==0)

class TestLeapYear(unittest.TestCase):

    def test_true_cases(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2004))

    def test_false_cases(self):
        self.assertFalse(is_leap_year(2025))
 
if __name__ == '__main__':
    unittest.main()





