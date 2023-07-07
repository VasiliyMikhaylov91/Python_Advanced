import csv


class Text:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if self.param1(value) and self.param2(value):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Bad {value}')


class Student:
    first_name = Text(str.istitle, str.isalpha)
    patronymic_name = Text(str.istitle, str.isalpha)
    last_name = Text(str.istitle, str.isalpha)

    def __init__(self, first_name: str, patronymic_name: str, last_name: str, objects_file_csv_path: str):
        self.first_name = first_name
        self.patronymic_name = patronymic_name
        self.last_name = last_name
        self._objects_results = {}
        with open(objects_file_csv_path, 'r', encoding='utf-8') as f:
            csv_file = csv.DictReader(f, fieldnames=['object', 'res', 'test res'])
            for line in csv_file:
                self._objects_results.update(
                    {line['object']: {'Оценка': int(line['res']), 'Результат теста': int(line['test res'])}})

    @property
    def average_res(self):
        sum_res = 0
        for item in self._objects_results.values():
            sum_res += item['Оценка']
        return sum_res / len(self._objects_results)

    @property
    def average_test_res(self):
        sum_res = 0
        for item in self._objects_results.values():
            sum_res += item['Результат теста']
        return sum_res / len(self._objects_results)

    @property
    def full_name(self):
        return f'{self._last_name} {self._first_name} {self._patronymic_name}'


if __name__ == '__main__':
    std = Student('Петр', 'Петрович', 'Петров', 'objects.csv')
    print(std.full_name)
    print(std.average_res)
    print(std.average_test_res)