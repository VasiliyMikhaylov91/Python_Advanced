# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


LOW_LIMIT = 0
MAX_LIMIT = 100000


def is_simple(number: int) -> bool:
    for i in range(2, number):
        if not number % i:
            return False
    return True


if __name__ == '__main__':
    input_number = int(input(f'Введите число от {LOW_LIMIT} до {MAX_LIMIT}: '))
    if LOW_LIMIT > input_number or input_number > MAX_LIMIT:
        print('Неподходящее число')
        quit()
    if is_simple(input_number):
        print('Число простое')
    else:
        print('Число составное')
