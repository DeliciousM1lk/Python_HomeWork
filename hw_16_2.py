"""
Модуль для проверки, является ли число степенью двойки.
"""

def is_power_of_two(n):
    """
    Проверяет, является ли число степенью двойки.
    :param n: целое число
    :return: True, если n — степень двойки, иначе False
    """
    return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    try:
        print(is_power_of_two(int(input("Введите число >>> "))))
    except ValueError as e:
        print(f"Вводите только числа!!!   {e}")
