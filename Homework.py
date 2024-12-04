# Task_1
while True:
    try:
        input_string = input("Введите строку из двух слов: ")
        word1, word2 = input_string.split()
        output_string = f"{word2} {word1}"
        print(output_string)
        break
    except ValueError:
        print("Вводите строку состоящую только из двух слов !!!")

# Task_2
word_count = len(input("Введите строку из слов, разделенных пробелами >>> ").strip().split())
print(f"Количество слов: {word_count}")

# Task_3
text = input("Введите строку с указанием 2020 года: ")
updated_text = text.replace('2020', '2024')
print("Обновленная строка:", updated_text)

