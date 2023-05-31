'''Создайте функцию-генератор.
Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило: “число является простым, если делится нацело только на единицу и на себя
'''


def simple_numbers(number: int):
    for i in range(2, number + 1):
        simple = True
        for j in range(2, i - 1):
            if not i % j:
                simple = False
                break
        if simple:
            yield i


print(*simple_numbers(50))
