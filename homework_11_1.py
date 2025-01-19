from inspect import isgenerator


def is_prime(x: int) -> bool:
    """Перерівка чи число є простим"""
    if x <= 1:  # Число не є 1 чи відʼємне
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def prime_generator(end: int) -> [int]:
    """Генерує прості числа в межі [2, end]."""
    current = 2
    while current <= end:
        if is_prime(current):  # Перевірка чи число є простим
            yield current  # Отримаємо число
        current += 1  # Рухаємося до наступного числа


gen = prime_generator(29)
print(list(gen))
