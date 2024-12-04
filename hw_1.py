def plus_two(a):
    try:
        return int(a) + 2
    except ValueError:
        return "Ожидаемый тип данных - число!"
    
    
if __name__ == "__main__":
    print(f"Результат : {plus_two(input('Введите число >>> '))}")