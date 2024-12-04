if __name__ == "__main__":
    numbers = []
    total_sum = 0

    while True:
        try:
            number = int(input("Введите число: "))
            numbers.append(number)
            total_sum += number

            if total_sum == 0:
                break
        except ValueError:
            print("Вводите только числа!!!")

    sum_of_squares = sum(num ** 2 for num in numbers)

    print("Сумма квадратов введённых чисел:", sum_of_squares)
