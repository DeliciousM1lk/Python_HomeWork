"""
Calculator
"""
import math

def display_menu():
    """
    Display the list of available operations.
    """
    print("Инженерный калькулятор")
    print("Доступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Квадратный корень (sqrt)")
    print("7. Факториал (factorial)")
    print("8. Число Фибоначчи (fibonacci)")
    print("9. Синус (sin)")
    print("10. Косинус (cos)")
    print("11. Тангенс (tan)")
    print("12. Выход")

def fibonacci(n):
    """
    Calculate the Fibonacci number.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def calculate_basic_operation(operation_type, x, y):
    """
    Perform basic arithmetic operations.
    """
    operations = {
        "add": x + y,
        "subtract": x - y,
        "multiply": x * y,
        "divide": x / y if y != 0 else "Ошибка: деление на ноль"
    }
    return operations.get(operation_type)

def calculate_square_root(x):
    """
    Calculate the square root.
    """
    return math.sqrt(x) if x >= 0 else "Ошибка: корень из отрицательного числа"

def calculate_factorial(x):
    """
    Calculate the factorial.
    """
    return math.factorial(x) if x >= 0 else "Ошибка: факториал отрицательного числа не существует"

def main():
    """
    Main function to handle user interaction and perform calculations.
    """
    display_menu()

    while True:
        choice = input("\nВведите номер операции : ")

        if choice == '12':
            print("Выход из калькулятора.")
            break

        if choice in {'1', '2', '3', '4'}:
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
            operation_type = {
                '1': "add",
                '2': "subtract",
                '3': "multiply",
                '4': "divide"
            }[choice]
            result = calculate_basic_operation(operation_type, x, y)
            print("Результат:", result)

        elif choice == '5':
            x = float(input("Введите число: "))
            y = float(input("Введите степень: "))
            print("Результат:", x ** y)

        elif choice == '6':
            x = float(input("Введите число: "))
            print("Результат:", calculate_square_root(x))

        elif choice == '7':
            x = int(input("Введите число: "))
            print("Результат:", calculate_factorial(x))

        elif choice == '8':
            x = int(input("Введите номер элемента Фибоначчи: "))
            print("Результат:", fibonacci(x))

        elif choice in {'9', '10', '11'}:
            x = float(input("Введите угол в радианах: "))
            trig_functions = {
                '9': math.sin,
                '10': math.cos,
                '11': math.tan
            }
            print("Результат:", trig_functions[choice](x))

        else:
            print("Ошибка: выбрана некорректная операция. Повторите ввод.")

if __name__ == "__main__":
    main()
