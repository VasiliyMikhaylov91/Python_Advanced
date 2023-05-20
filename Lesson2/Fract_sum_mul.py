from fractions import *


def greatest_common_divisor(number1: int, number2: int) -> int:
    if number1 == number2:
        return number1
    if number1 > number2:
        return greatest_common_divisor(number2, number1)
    if not number1:
        return number2
    return greatest_common_divisor(number1, number2 - number1)


def split_fraction(fraction: str) -> list[int, int]:
    return list(int(item) for item in fraction.split('/'))


def reduce_fraction(fraction: str) -> str:
    fraction_list = split_fraction(fraction)
    gcd = greatest_common_divisor(fraction_list[0], fraction_list[1])
    return f'{int(fraction_list[0] / gcd)}/{int(fraction_list[1] / gcd)}'


def least_common_multiple(number1: int, number2: int) -> int:
    return int((number1 * number2) / greatest_common_divisor(number1, number2))


def sum_fractions(fraction1: str, fraction2: str) -> str:
    fraction1_list = split_fraction(fraction1)
    fraction2_list = split_fraction(fraction2)
    lcm = least_common_multiple(fraction1_list[1], fraction2_list[1])
    numerator = int(fraction1_list[0] * lcm / fraction1_list[1]) + int(fraction2_list[0] * lcm / fraction2_list[1])
    return reduce_fraction(f'{numerator}/{lcm}')


def mul_fractions(fraction1: str, fraction2: str) -> str:
    fraction1_list = split_fraction(fraction1)
    fraction2_list = split_fraction(fraction2)
    return reduce_fraction(f'{fraction1_list[0] * fraction2_list[0]}/{fraction1_list[1] * fraction2_list[1]}')


def sum_mul_fractions(fraction1: str, fraction2: str) -> tuple[str, str]:
    return sum_fractions(fraction1, fraction2), mul_fractions(fraction1, fraction2)


if __name__ == '__main__':
    print(sum_mul_fractions('3/8', '2/5'))
    print(Fraction(3, 8) + Fraction(2, 5), Fraction(3, 8) * Fraction(2, 5))
