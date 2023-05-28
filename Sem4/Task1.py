'''Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы
Слова выводятся отсортированными согласно кодировки Unicode
Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки
'''


def task1(inp: str) -> None:
    text_list = inp.split()
    text_list.sort()
    # for item in text_list:
    #     if len(item) > max_length:
    #         max_length = len(item)
    max_length = len(max(text_list, key=len))
    for number, item in enumerate(text_list, start=1):
        print(f'{number} {item:>{max_length}}')

task1('adad adarfwfwe saa ferge')