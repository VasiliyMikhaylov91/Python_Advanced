# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for _ in range(10):
    input_number = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    if num == input_number:
        print('Вы угадали число')
        break
    elif num < input_number:
        print('Меньше')
    else:
        print('Больше')
else:
    print('Повезёт в другой раз')