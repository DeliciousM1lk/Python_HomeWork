"""
Этот код выравнивает строки по самой длинной строке, добавляя звездочки.
Для каждой строки выводится соответствующее количество звездочек перед строкой.
"""
def align_strings(str_list):
    """
    Эта функция выравнивает строки по самой длинной строке, добавляя звездочки.
    Для каждой строки выводится соответствующее количество звездочек перед строкой.
    """
    max_length = max(len(s) for s in str_list)
    for s in str_list:
        print('*' * (max_length - len(s)) + s)

if __name__ == "__main__":
    M = int(input("Введите количество строк: "))
    str_lst = [input() for _ in range(M)]
    max_len = max(len(s) for s in str_lst)
    print(max_len)
    align_strings(str_lst)
