# # Task 1
while True:
    try:
        N = int(input("Введите количество карточек: "))

        remaining_sum = 0

        print("Введите номера оставшихся карточек:")

        for i in range(N - 1):
            card = int(input("Введите номер: "))
            remaining_sum += card
        total_sum = N * (N + 1) // 2
        missing_card = total_sum - remaining_sum

        print("Потерянная карточка:", missing_card)
        break

    except ValueError:
        print("Вводите только числа !!!")


# Task 2

while True:
    try:
        N = int(input("Введите число N >>> "))
        i = 1
    except ValueError:
        print("Вводите только целые числа!!!")
        continue

    while i * i <= N:
        print(i * i)
        i += 1
    break

    