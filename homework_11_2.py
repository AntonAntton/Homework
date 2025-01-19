def is_cube(x: int) -> bool:
    """Перевіряє чи цифра є цілочисельним кубом."""
    if x < 0:
        return False
    cube_root = round(x ** (1 / 3))
    return cube_root ** 3 == x


def generator_cube_numbers(start: int, end: int):
    """
    Генерує цифри які є цілочисельними кубами.
    """
    current = start
    while True:
        if is_cube(current):
            yield current
        current += 1
        if end is not None and current > end:
            break


# Вислик функції
gen = generator_cube_numbers(1, 100)
print(list(gen))
