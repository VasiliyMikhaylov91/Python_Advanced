'''
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где
ключ - тип элемента,
значение - список элементов данного типа
'''

def task3():
    input_tuple = (3, 5, "asd", True, 5.45, False, "jlh", 8.4)
    result_dict = {}
    for i in input_tuple:
        if type(i) not in result_dict.keys():
            result_dict[type(i)] = []
        result_dict[type(i)].append(i)

    print(result_dict)


task3()