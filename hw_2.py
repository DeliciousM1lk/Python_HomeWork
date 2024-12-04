"""
Модуль для нахождения всех уникальных слов, которые можно составить
из заданной последовательности символов, с учётом ограничений
на количество повторений символов.
"""

from itertools import permutations
from collections import Counter

def find_words(sequence):
    """
    Выводит количество уникальных слов, составленных из букв
    последовательности, и сами слова, отсортированные по длине и
    лексикографически.
    """
    char_count = Counter(sequence)

    unique_words = set()

    for length in range(1, len(sequence) + 1):
        for perm in permutations(sequence, length):
            word = ''.join(perm)
            word_count = Counter(word)

            if all(word_count[char] <= char_count[char] for char in word):
                unique_words.add(word)

    sorted_words = sorted(unique_words, key=lambda x: (len(x), x))

    print(len(sorted_words))
    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    SEQUENCE = "k98.ok"
    find_words(SEQUENCE)
