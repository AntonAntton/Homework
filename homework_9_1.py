def popular_words(text, words):
    # Рахуємо кількісль слів з тексту користувача
    text = text.lower().split()

    word_count = {}
    for word in words:
        word_count[word] = text.count(word)

    return word_count


# Запрос від користувача на текст і слова
input_text = input("Enter your text: ")
input_words = input("Enter your words: ").split(",")

#Визиваємо функцію popular_words і рахуємо слова
word_count = popular_words(input_text, input_words)

# Роздруковуємо результат
for word, count in word_count.items():
    print(f"{word}: {count}")