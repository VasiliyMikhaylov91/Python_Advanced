'''Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию
'''

def task2(inp: str) -> list[int]:
    result = set()
    for i in inp:
        result.add(ord(i))
    return sorted(result, reverse=True)

print(task2('bdr ssfhtth  zcvnnmo'))