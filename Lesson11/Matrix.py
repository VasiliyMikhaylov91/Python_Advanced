from copy import copy


class Matrix:
    def __init__(self, values: list[list[float]]):
        self.values = values
        self.height = len(values)
        self.length = len(values[0])
        if self.height > 1:
            for row in range(1, self.height):
                if len(self.values[row]) != self.length:
                    raise AttributeError('Строки матрицы должны иметь одинаковое количество значений')

    def __add__(self, other):
        if self.height != other.height or self.length != other.length:
            raise AttributeError('Матрицы должны иметь одинаковое количество строк и столбцов')
        new_matrix = copy(self.values)
        for row in range(self.height):
            for col in range(self.length):
                new_matrix[row][col] = self.values[row][col] + other.values[row][col]
        return Matrix(new_matrix)

    def __str__(self):
        res = ''
        for row in range(self.height):
            res += ' '.join(map(str, self.values[row])) + '\n'
        return res

    def sum_elements(self) -> float:
        summ = 0.0
        for row in range(self.height):
            for col in range(self.length):
                summ += self.values[row][col]
        return summ

    def __eq__(self, other):
        if self.height != other.height or self.length != other.length:
            return False
        for row in range(self.height):
            for col in range(self.length):
                if self.values[row][col] != other.values[row][col]:
                    return False
        return True

    def __gt__(self, other):
        return self.sum_elements() > other.sum_elements()

    def __ge__(self, other):
        return not self.__gt__(other)

    def __lt__(self, other):
        return self.sum_elements() < other.sum_elements()

    def __le__(self, other):
        return not self.__lt__(other)


if __name__ == '__main__':
    m1 = Matrix([[2.0, 4.3], [1.0, 5.1]])
    print(m1)
    m2 = Matrix([[4.0, 1.5], [3.0, 6.4]])
    print(m2)
    print(m1 + m2)
    print(f'{m1 == m2 = }')
    print(f'{m1 != m2 = }')
    print(f'{m2 >= m1 = }')
