'''Функция получает на вход список чисел и два индекса.
Вернуть сумму чисел между между переданными индексами.
Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
'''

def task6(numbers: list[int], index_min: int, index_max: int) -> int:
    if index_min > index_max:
        task6(numbers, index_max, index_min)
    if index_min < 0:
        index_min = 0
    if index_max > len(numbers) - 1:
        index_max = len(numbers) - 1

    return sum(numbers[index_min: index_max + 1])

print(task6([1,2,3,4,5], -10, 20))