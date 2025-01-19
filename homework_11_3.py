def is_even(digit: int) -> bool:
    """
    Функція перевіряє чи число парне, чи непарне і повертає True чи False.
    """
    return not digit & 1


# Перевіряємо функцію
print(is_even(2494563894038**2))
print(is_even(1056897**2))
