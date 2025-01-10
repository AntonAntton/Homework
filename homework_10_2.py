import string
import re

def first_word(text: str) -> str:
    """
    Функція повертає перше слово з тексту користувача,
    видаляє пунктуацію (за винятком одинарних лапок) і розділяє слова
    за наявності пробілу чи заглавної літери.

    Параметри:
    text (str): Текст для аналізу.

    Повертає:
    str: Перше слово з тексту або "No words found".
    """
    # Розділяємо текст на окремі слова, якщо в текст є пробіли
    # чи слова починаються з заглавної літери.
    if " " in text:
        words = text.split()
    else:
        words = re.findall(r'[A-Z][^A-Z]*', text)
        if not words:
            words = [text]

    # Повертаємо перше слово з розділеного тексту.
    return words[0] if words else "No words found"


# Запит від користвувача на текст
my_text = input("Enter your text: ")

# Видаляємо пунктуацію з тексту(не враховуєчи одинарні лапки)
punctuation_to_remove = string.punctuation.replace("'", "")
my_text = my_text.translate(str.maketrans("", "", punctuation_to_remove))

# Визиваємо функцію
print(first_word(my_text))
