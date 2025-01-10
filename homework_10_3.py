def is_even(digit: int) -> bool:
    """
    Функція перевіряє чи число парне, чи непарне і повертає True чи False.

    Параметри:
    digit (int): Ціле число для перевірки.

    Повертає:
    bool: True, якщо число парне; False, якщо непарне.
    """
    return True if digit % 2 == 0 else False


# Перевіряємо функцію
print(is_even(4))
print(is_even(5))
