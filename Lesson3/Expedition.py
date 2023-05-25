def sum_weight(contain: dict[str:int]) -> int:
    result = 0
    for item in contain:
        result += contain[item]
    return result


def dispersal(contain: dict[str:int], bag_capacity: int) -> list[set]:
    result = []
    bag = set()

    while contain:
        item, weihgt = contain.popitem()
        if weihgt <= bag_capacity:
            bag.add(item)
            bag_capacity -= weihgt

    result.append(bag)

    return result


if __name__ == '__main__':
    print(dispersal({'pot': 6, 'carrot': 2, 'lantern': 5}, 7))