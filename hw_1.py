"""
Этот код сортирует список
"""
def insertion_sort(lst):
    """
    Эта функция сортирует список в порядке возрастания
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

if __name__ == "__main__":
    numbers = [1, 4, 2, 3, 4]
    print(insertion_sort(numbers))
