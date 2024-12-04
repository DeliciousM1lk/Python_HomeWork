# # Task 1
# inputed_diameter = float(input("Введите диаметр окружности : "))
# value_of_pi = 3.14
# L = value_of_pi * inputed_diameter
# print(f"Длина окружности: {round(L, 2)}")



# # Task 2
# inputed_radius = float(input("Введите радиус окружности:"))
# value_of_pi = 3.14
# L = 2 * value_of_pi * inputed_radius
# S = value_of_pi * (inputed_radius ** 2)
# print(f"Длинна окружности: {round(L, 2)}")
# print(f"Площадь круга: {round(S, 2)}")


#  Task 3
inputed_1 = float(input("Введите первое число : "))
inputed_2 = float(input("Введите второе число : "))

if inputed_1 < 0 or inputed_2 < 0:
    
    print("Числа должны быть положительными\n")

else:
    result_ = (inputed_1 * inputed_2) ** 0.5
    print(f"Среднее геометричекое : {round(result_, 2)}")


# # Task 4
# inputed_length = float(input("Введите длинну окружности :"))
# value_of_pi = 3.14

# R = inputed_length / (2 * value_of_pi)
# S = value_of_pi * (R ** 2)

# print(f"Радиус окружности : {round(R, 2)}")
# print(f"Площадь круга : {round(S, 2)}")

# # Task 5
# while True:
#     try:
#         inputed_value = (int(input("Введите целое число : ")))
#         Answer = 3 * (inputed_value**2) - (6 * inputed_value) - 7
#         print(f"Ответ : {Answer}")
#         break
#     except ValueError:
#         print("Введите целое число!")

# # Task 6
# while True:
#     try:
#         inputed_value = (int(input("Введите целое число : ")))
#         Answer = 4 * (inputed_value - 3) - (7 * (inputed_value - 3)) + 2
#         print(f"Ответ : {Answer}")
#         break
#     except ValueError:
#         print("Введите целое число!")
    

