"""
Этот код показывает числа из данного списка с наименьшей разностью и сортирует их.
"""
def find_closest_pair(numbers):
    """
    Эта функция находит два ближайших числа и сортирует в порядке возрастания.
    """
    numbers.sort()
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[1])

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

if __name__ == "__main__":
    numbers_list = list(map(int, input("Введите список чисел через пробел: ").split()))
    result = find_closest_pair(numbers_list)
    print(result[0], result[1])
