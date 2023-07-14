import pytest
from Date_validation_doctest import is_date_valid


def test_some_valid_date():
    assert is_date_valid('21.04.1991'), 'Some valid date failed'


def test_some_invalid_date():
    assert not is_date_valid('30.02.2001'), 'Some invalid date failed'


def test_february_non_leap_year():
    assert not is_date_valid('29.02.2300'), "29 February can't be in non leap year"


def test_february_leap_year():
    assert is_date_valid('29.02.2000'), "29 February mast be in leap year"


def test_invalid_str_input():
    assert not is_date_valid("It's not date"), "Mast be False if input have not format DD.MM.YYYY"


if __name__ == '__main__':
    pytest.main()