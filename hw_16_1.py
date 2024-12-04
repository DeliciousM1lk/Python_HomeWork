"""
Модуль для вычисления чисель Фибоначчи
"""
def fibonacci(n):
    """Возвращает n-е число Фибоначчи."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """Выводит первые 10 чисел Фибоначчи."""
    for i in range(1, 11):
        print(f"fibonacci number {i} = {fibonacci(i)}")

if __name__ == "__main__":
    main()
