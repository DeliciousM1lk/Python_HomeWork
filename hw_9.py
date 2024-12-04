"""
Код для разделения строки по нескольким разделителям.
"""

def split_string_by_multiple_delimiters(text_to_split, delimiters_list):
    """
    Функция разделяет строку на части, используя несколько разделителей.
    """
    result_list = [text_to_split]
    for delimiter in delimiters_list:
        temp_result = []
        for part in result_list:
            temp_result.extend(part.split(delimiter))
        result_list = temp_result
    return [part for part in result_list if part]

if __name__ == "__main__":
    user_input_text = input("Введите строку: ")
    user_input_delimiters = input("Введите разделители (каждый разделитель через пробел): ").split()
    split_result = split_string_by_multiple_delimiters(user_input_text, user_input_delimiters)
    print("Результат:", split_result)
