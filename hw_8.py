"""
Этот код извлекает слова, начинающиеся на гласную букву
"""
def extract_words_starting_with_vowel(text):
    """
    Эта функция извлекает слова, начинающиеся на гласную букву
    """
    vowels = "aeiouAEIOU"
    words = text.split()
    result = [word for word in words if word[0] in vowels]
    return result

if __name__ == "__main__":
    text_str = input("Введите текст: ")
    words_with_vowels = extract_words_starting_with_vowel(text_str)
    print("Слова, начинающиеся на гласную:", words_with_vowels)
