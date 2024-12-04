def access_array_element(array, index):
    try:
        return array[index]
    except IndexError:
        return "Ошибка: Индекс выходит за границы массива!"


if __name__ == "__main__":
    my_array = [10, 20, 30, 40, 50]
    print(f"Результат: {access_array_element(my_array, int(input("Введите индекс >>> "))-1)}")
    
