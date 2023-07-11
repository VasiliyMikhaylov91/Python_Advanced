from copy import copy


class Matrix_Row_Exception(AttributeError):
    def __str__(self):
        return 'Строки матрицы должны иметь одинаковое количество значений'


class Matrix_Add_Exception(AttributeError):
    def __init__(self, matrix1_rows_number: int, matrix2_rows_number: int,
                 matrix1_column_number: int, matrix2_column_number: int):
        self.m1_rows = matrix1_rows_number
        self.m2_rows = matrix2_rows_number
        self.m1_col = matrix1_column_number
        self.m2_col = matrix2_column_number

    def __str__(self):
        return f'Матрицы должны иметь одинаковое количество строк и столбцов\n' \
               f'У первой матрицы {self.m1_rows} строк, у второй {self.m2_rows}\n' \
               f'У первой матрицы {self.m1_col} столбцов, у второй {self.m2_col}'


class Matrix:
    def __init__(self, values: list[list[float]]):
        self.values = values
        self.height = len(values)
        self.length = len(values[0])
        if self.height > 1:
            for row in range(1, self.height):
                if len(self.values[row]) != self.length:
                    raise Matrix_Row_Exception

    def __add__(self, other):
        if self.height != other.height or self.length != other.length:
            raise Matrix_Add_Exception(self.height, other.height, self.length, other.length)
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
    # m1 = Matrix([[2.0, 4.3], [1.0]])
    m2 = Matrix([[4.0, 1.5], [3.0, 6.4]])
    m3 = Matrix([[3.1], [6.7]])
    print(m3 + m2)
