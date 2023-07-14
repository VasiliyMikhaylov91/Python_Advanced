import unittest
from Date_validation_doctest import is_date_valid


class TestCaseName(unittest.TestCase):

    def test_some_valid_date(self):
        self.assertTrue(is_date_valid('21.04.1991'), msg='Some valid date failed')

    def test_some_invalid_date(self):
        self.assertFalse(is_date_valid('30.02.2001'), msg='Some invalid date failed')

    def test_february_non_leap_year(self):
        self.assertFalse(is_date_valid('29.02.2300'), msg="29 February can't be in non leap year")

    def test_february_leap_year(self):
        self.assertTrue(is_date_valid('29.02.2000'), msg="29 February mast be in leap year")

    def test_invalid_str_input(self):
        self.assertFalse(is_date_valid("It's not date"), msg="Mast be False if input have not format DD.MM.YYYY")


if __name__ == '__main__':
    unittest.main(verbosity=1)