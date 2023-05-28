'''Функция получает на вход список чисел.
Отсортируйте его элементы in place без использования встроенных в язык сортировок.
Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
'''


def task4(inp: list[int]) -> list[int]:
    if len(inp) > 1:
        for i in range(len(inp) - 1):
            for j in range(len(inp) - 1 - i):
                if inp[j] > inp[j + 1]:
                    temp = inp[j]
                    inp[j] = inp[j + 1]
                    inp[j + 1] = temp
    return inp


print(task4([2, 3, 8, 4, 5]))
