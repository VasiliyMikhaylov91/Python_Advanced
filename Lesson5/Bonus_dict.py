def bonus_dict(names: list[str], rates: list[int], bonuses: list[str]) -> dict[str: float]:
    return {names[i]: rates[i] + rates[i] * (float(bonuses[i][:-1]) / 100) for i in range(len(names))}


if __name__ == '__main__':
    print(bonus_dict(['stark', 'black', 'parker'], [80000, 100000, 50000], ['12.03%', '30.5%', '8.14%']))
