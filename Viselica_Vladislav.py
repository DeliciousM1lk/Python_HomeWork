import random

stages = [
    """
       -----
       |   |
       O   |
      /|\  |
      / \>8|
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
    8</    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\>8|
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
   8< /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       | >8|
           |
           |
    =========
    """,
    """
       -----
       |   |
    8< O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """
]

words = ["апельсин", "программирование", "гадание", "игра", "виселица"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = set()

print("Добро пожаловать в игру Виселица!")

while attempts > 0 and "_" in guessed:
    print(stages[6 - attempts])
    print("Текущий статус:", " ".join(guessed))
    print("Осталось попыток:", attempts)
    print("Уже угаданные буквы:", " ".join(sorted(guessed_letters)))

    guess = input("Введите букву: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Пожалуйста, введите одну букву.")
        continue

    if guess in guessed_letters:
        print("Вы уже угадали эту букву.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Правильно!")
        for index, letter in enumerate(word):
            if letter == guess:
                guessed[index] = guess
    else:
        print("Неправильно!")
        attempts -= 1

if "_" not in guessed:
    print("Поздравляем! Вы угадали слово:", word)
else:
    print(stages[6]) 
    print("Игра окончена, вы проиграли! Загаданное слово было:", word)