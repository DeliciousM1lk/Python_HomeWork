"""
Код для обработки списка чисел, разделяющий их на четные и нечетные, а также проверяющий,
какая группа чисел больше.
"""

def check_numbers(num_list):
    """
    Эта функция разделяет четные и нечетные числа, печатает их и проверяет, какая группа больше.
    """
    odd_numbers = []
    even_numbers = []

    for num in num_list:
        if num % 2 != 0:
            odd_numbers.append(num)
        else:
            even_numbers.append(num)

    print(" ".join(str(num) for num in odd_numbers))
    print(" ".join(str(num) for num in even_numbers))

    if len(odd_numbers) > len(even_numbers):
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    check_numbers(numbers)
