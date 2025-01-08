import string
import re


def first_word():
    """
    Функція повертає перше слово з тексту користучава,
    видаляє пунктуацію(за вийнятком одинарних лапок) і розділяє слова
    за наявності пробілу чи заглавної літери.
    """
    # Запит від користвувача на текст
    my_text = input("Enter your text: ")

    # Видаляємо пунктуацію з тексту(не враховуєчи одинарні лапки)
    punctuation_to_remove = string.punctuation.replace("'", "")
    my_text = my_text.translate(str.maketrans("", "", punctuation_to_remove))

    # Розділяємо текст на окремі слова, якщо в текст є пробіли, чи слова починаються з заглавної літери.
    if " " in my_text:
        words = my_text.split() 
    else:
        words = re.findall(r'[A-Z][^A-Z]*', my_text)
        if not words:
            words = [my_text]

    print(f"Words after split: {words}")

    # Повертаємо перше слово з розділеного тексту.
    return words[0] if words else "No words found"

# Визиваємо функцію
print(first_word())