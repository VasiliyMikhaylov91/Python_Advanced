from math import sqrt


def square_solution(a: float, b: float, c: float) -> tuple:
    d = b ** 2 - 4 * a * c
    if d < 0:
        j = sqrt(-d) / a / 2
        return complex(-b / a / 2, j), complex(-b / a / 2, -j)
    return (-b + sqrt(d)) / a / 2, (-b - sqrt(d)) / a / 2


if __name__ == '__main__':
    print(square_solution(4, 1, 2))
