'''
Вручную создайте список с целыми числами, которые повторяются.
Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
*Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков
'''

def uniq_elements(array: list[int]) -> list[int]:
    result = []
    for item in array:
        if item not in result:
            result.append(item)
    return result

def uniq_elements(array: list[int]) -> list[int]:
    return list(set(array))