'''
Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
'''


def del_doubles(inp: list) -> list:
    temp_dict = dict()
    res = []
    for item in inp:
        if item not in temp_dict:
            temp_dict.update({item: 0})
        temp_dict[item] += 1

    for item in inp:
        if temp_dict[item] != 2:
            res.append(item)
    return res

print(del_doubles([2,2,2,2,3,3,3,4,5,5,7,8]))