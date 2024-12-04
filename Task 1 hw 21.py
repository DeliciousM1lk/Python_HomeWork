
lang = input("""
1. English
2. Русский 
Выберите язык >>> """)
shift = int(input("Введите сдвиг: "))
text = input("Введите текст: ")

eng_alphabet = ' abcdefghijklmnopqrstuvwxyz'
rus_alphabet = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
result = ''

if lang == "1":
    for char in text:
        if char in eng_alphabet:
            old_index = eng_alphabet.index(char)
            new_index = (old_index + shift) % len(eng_alphabet)
            result += eng_alphabet[new_index]
        else:
            result += char
            
else:
    for char in text:
        if char in rus_alphabet:
            old_index = rus_alphabet.index(char)
            new_index = (old_index + shift) % len(rus_alphabet)
            result += rus_alphabet[new_index]
        else:
            result += char

print("Зашифрованный текст: ", result)


