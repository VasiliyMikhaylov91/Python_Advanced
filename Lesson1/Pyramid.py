def pyramid(row_number: int):
    for i in range(row_number):
        print(' ' * (row_number - i - 1) + '*' * (2 * i + 1))


if __name__ == '__main__':
    pyramid(int(input('Сколько строк у ёлки? ')))
