"""

Этот код решает задачу, при которой нужно добавить к массиву элемент.
"""
def balance_sums(arr):
    """
    Эта функция добавляет к массиву элемент, чтобы сумма положительных чисел
    в массиве стала равной по модулю сумме отрицательных чисел.
    """
    sum_positive = sum(x for x in arr if x > 0)
    sum_negative = sum(x for x in arr if x < 0)

    if sum_positive != -sum_negative:
        diff = sum_positive + sum_negative
        if sum_positive > 0:
            arr.append(diff)
        else:
            arr.append(-diff)
    return arr

if __name__ == "__main__":
    arr_1 = list(map(int, input("Введите массив чисел через пробел: ").split()))
    result = balance_sums(arr_1)
    print(result)
