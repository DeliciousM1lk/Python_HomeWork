"""
Модуль для создания матрицы 3x3 и вычисления суммы элементов главной диагонали.
"""

def create_matrix_and_sum_diagonal():
    """
    Создает матрицу 3x3 с вводом данных от пользователя и вычисляет сумму
    элементов главной диагонали.
    """
    matrix = []

    for i in range(3):
        while True:
            row = input(f"Введите строку {i + 1} через пробел (3 числа): ").split()
            if len(row) == 3:
                try:
                    int_row = []
                    for num in row:
                        int_row.append(int(num))
                    matrix.append(int_row)
                    break
                except ValueError:
                    print("Ошибка: Вводите только целые числа. Попробуйте еще раз.")
            else:
                print("Ошибка: Должно быть ровно 3 числа. Попробуйте еще раз.")

    diagonal_sum = sum(matrix[i][i] for i in range(3))

    print("Матрица:")
    for row in matrix:
        print(row)

    print(f"Сумма элементов главной диагонали: {diagonal_sum}")
    return diagonal_sum


if __name__ == "__main__":
    create_matrix_and_sum_diagonal()
