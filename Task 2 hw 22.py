import os
eng_french = {}
while True:
    try:
        action = int(input("""\n Что делаем со словарём?
                           
        1- Добавление слова
        2 - Удаление слова
        3 - Поиск перевода
        4 - Замена слова
        5 - Показать словарь
        6 - Выход из словаря (Данные словаря будут удалены!!!)
        0 - Мне не нравится словарь!   
        >>> """))
        if action == 1:
            word_n_translation_to_add = {input("Введите слово для добавления: ") : input("Введите перевод слова на франзуском: ")}
            eng_french.update(word_n_translation_to_add)
            print("Слово добавлено!!!")

        elif action == 2:
            eng_french.pop(input("Введите слово для удаления: "))
            print("Слово удалено!!!")

        elif action == 3:
            word_to_find = input("Введите слово для поиска в словаре: ")
            print(eng_french[word_to_find])

        elif action == 4:
            word_to_replace = input("Введите слово для замены: ")
            replacement = {input("Введите слово на английском: "): input("Введите перевод слова на французском: ")}
            eng_french.pop(word_to_replace)
            eng_french.update(replacement)
            print("Слово заменено!!!")
        
        elif action == 5:
            print(eng_french)

        elif action == 6:
            exit

        elif action == 0:
            os.remove('Task 2 hw 22.py')
        
        else:
            print("Введите правильное зачение!!!")

    except ValueError:
        print("Введите число!!!")

