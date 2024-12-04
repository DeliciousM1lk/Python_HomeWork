# Task 1
# while True:
#     try:
#         n = int(input("Введите натуральное число n >>> "))

#         sum_factorials = 0
#         current_factorial = 1
#         for i in range(1, n + 1):
#             current_factorial *= i
#             sum_factorials += current_factorial

#         print("Сумма 1! + 2! + ... +", n, "!", "=", sum_factorials)
#         break
#     except ValueError:
#         print("Вводите только числа!!!")

# Task 2
while True:
    try:
        n = int(input("Введите натуральное число n (n ≤ 9): "))
        if 1 <= n <= 9:
            for i in range(1, n + 1):
                step = ""
                for j in range(1, i + 1):
                    step += str(j)
                print(step)
                
                
    except ValueError:
        print("Ошибка: n должно быть натуральным числом и не больше 9.")
    