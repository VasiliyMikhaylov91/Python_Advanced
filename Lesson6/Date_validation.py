from sys import argv

MIN_YEAR = 1
MAX_YEAR = 9999
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31
MAX_DAY_LOW_MONTH = 30
MAX_DAY_SPECIAL_MONTH = 28
MAX_DAY_SPECIAL_MONTH_IN_LEAP = 29
LOW_MONTHS = (4, 6, 9, 11)
SPECIAL_MONTH = 2


def _is_leap_year(year: int) -> bool:
    return (not year % 4 and year % 100) or not year % 400


def _is_year_valid(year: int) -> bool:
    return MIN_YEAR <= year <= MAX_YEAR


def _is_month_valid(month: int) -> bool:
    return MIN_MONTH <= month <= MAX_MONTH


def _is_day_valid(day: int, month: int, year: int) -> bool:
    min_day = MIN_DAY
    if month == SPECIAL_MONTH:
        max_day = MAX_DAY_SPECIAL_MONTH_IN_LEAP if _is_leap_year(year) else MAX_DAY_SPECIAL_MONTH
    elif month in LOW_MONTHS:
        max_day = MAX_DAY_LOW_MONTH
    else:
        max_day = MAX_DAY
    return min_day <= day <= max_day


def is_date_valid(date: str) -> bool:
    date_list = date.split('.')
    if len(date_list) != 3 or not date.replace('.', '').isdigit():
        return False
    date_list = list(map(int, date_list))
    return _is_year_valid(date_list[2]) and _is_month_valid(date_list[1]) and _is_day_valid(*date_list)


if __name__ == '__main__':
    print(is_date_valid(argv[1]))
