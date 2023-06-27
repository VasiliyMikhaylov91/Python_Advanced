import csv
import json
from random import uniform, randint
from typing import Callable, Dict, Any, Iterable


def csv_random_numbers_gen(file_name: str, lower_limit: float, upper_limit: float, row_number: int) -> None:
    if not file_name.endswith('.csv'):
        file_name.replace('.', '')
        file_name += '.csv'
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        csv_write = csv.DictWriter(f, fieldnames=['a', 'b', 'c'], dialect='excel-tab')
        for _ in range(row_number):
            row = {'a': uniform(lower_limit, upper_limit),
                   'b': uniform(lower_limit, upper_limit),
                   'c': uniform(lower_limit, upper_limit)}
            csv_write.writerow(row)


def rows_from_csv(file_name: str) -> Callable[[Callable[..., Any]], dict]:
    def wrapper(funct: Callable) -> dict:
        result = {}
        with open(file_name, 'r') as f:
            csv_file = csv.DictReader(f, fieldnames=['a', 'b', 'c'], dialect='excel-tab')
            for line in csv_file:
                line_name = line['a'], line['b'], line['c']
                if (name := ' '.join(line_name)) not in result:
                    result[name] = funct(*map(float, line_name))
        return result

    return wrapper


def dict_to_json(file_name: str) -> Callable[[Iterable], None]:
    if not file_name.endswith('.json'):
        file_name.replace('.', '')
        file_name += '.json'

    def wrapper(funct: Iterable):
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(funct, f, ensure_ascii=False)

    return wrapper


csv_random_numbers_gen('some', -30, 30, randint(100, 1000))


@dict_to_json('res')
@rows_from_csv('some.csv')
def square_root(a: float, b: float, c: float) -> (float, float) or float or str:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return 'Нет корней'
    elif not discriminant:
        return (discriminant ** 0.5 - b) / 2 / a
    else:
        return (discriminant ** 0.5 - b) / 2 / a, (- discriminant ** 0.5 - b) / 2 / a
