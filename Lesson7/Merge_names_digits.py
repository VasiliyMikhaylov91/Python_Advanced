from pathlib import Path
from typing import TextIO


def _str_from_file(field: TextIO):
    line = field.readline()
    if not line:
        field.seek(0)
        return _str_from_file(field)
    return line[:-1]


def merge(names_path: str, digits_path: str, result_path: str):
    names_length = len(names_path)
    digits_length = len(digits_path)
    with (open(names_path, 'r', encoding='utf-8') as names,
          open(digits_path, 'r', encoding='utf-8') as digits,
          open(result_path, 'w', encoding='utf-8') as result
          ):
        for _ in range(max(names_length, digits_length)):
            digs = _str_from_file(digits).split('|')
            name = _str_from_file(names)
            mult = int(digs[0]) * float(digs[1])
            if mult > 0:
                result.write(f'{name.upper()} {round(mult)}\n')
            elif mult < 0:
                result.write(f'{name.lower()} {abs(mult)}\n')


if __name__ == '__main__':
    merge('names.txt', 'num.txt', 'merge.txt')
