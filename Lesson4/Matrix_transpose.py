def transpose(matrix: list[list[int]]) -> list[list[int]] | str:
    length = len(matrix)
    column_length = len(matrix[0])

    if length > 1:
        for i in range(1, length):
            if len(matrix[i]) != column_length:
                return 'Ошибка ввода матрицы - несоответствие количества столбцов'

    result = []
    for i in range(column_length):
        result.append([])
        for j in range(length):
            result[i].append(matrix[j][i])
    return result


if __name__ == '__main__':
    print(transpose([[1, 2, 3], [4, 5]]))
    print(transpose([[1, 2], [3, 4], [5, 6]]))
    print(transpose([[1, 2, 3]]))
    print(transpose([[1], [2], [3]]))
