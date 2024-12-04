while True:
    try:
        first_team = int(input("Введите число человек в первой команде >>> "))
        second_team = int(input("Введите число человек во второй команде >>> "))
        x, y = first_team, second_team

        while y != 0:
            x, y = y, x % y

        answer = (first_team * second_team) // x
        print("Минимальное подходящее число кусочков пирога:", answer)
        break

    except ValueError:
        print("Вводите только числа!!!")
