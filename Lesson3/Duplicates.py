def duplicates(input_list: list) -> list:
    temp_dict = dict()
    result = []

    for item in input_list:
        if item not in temp_dict:
            temp_dict.update({item: 0})
        temp_dict[item] += 1

    for key in temp_dict:
        if temp_dict[key] > 1:
            result.append(key)

    return result


if __name__ == '__main__':
    print(duplicates([2, 3, 3, 3, 'as', 'as', 'd', 4, 4]))
