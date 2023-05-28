'''Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет символ из Unicode, а значением - целое число.
Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно
'''


def task3(inp: str) -> dict[int: int]:
    num1, num2 = tuple(map(int, inp.split()))
    min_number = min(num1, num2)
    max_number = max(num1, num2)
    result = dict()
    for i in range(min_number, max_number + 1):
        result.update({chr(i): i})
    return result


print(task3('10 99'))