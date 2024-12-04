"""
Этот код сортирует список
"""
def selection_sort(arr):
    """
    Эта функция сортирует числа в порядке убывания
    """
    sorted_arr = []
    while arr:
        max_element = max(arr)
        sorted_arr.append(max_element)
        arr.remove(max_element)
    return sorted_arr


if __name__ == "__main__":
    numbers = [1, 4, 2, 3, 4]
    print(selection_sort(numbers))
