from random import randint, uniform


def rand_int_float(row_numbers: int, file_name: str, min_number: int = -1000, max_number: int = 1000):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(row_numbers):
            f.write(f'{randint(min_number, max_number)}|{uniform(min_number, max_number)}\n')


if __name__ == '__main__':
    rand_int_float(6, 'num.txt')