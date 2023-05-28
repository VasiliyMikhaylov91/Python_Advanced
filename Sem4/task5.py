'''Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида “10.25%”.
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
'''


def task5(names: list[str], rate: list[int], bonus: list[str]) -> dict[str: float]:
    length = len(names)

    result = dict()

    for i in range(length):
        result.update({names[i]: rate[i] + rate[i] * (float(bonus[i].replace('%', '')) / 100)})

    return result


print(task5(['Иванов', 'Петров', 'Сидоров'], [40000, 35000, 60000], ['10.25%', '12.2%', '8.65%']))
