from inspect import isgenerator


def pow(x):
    """Повертає корінь квадратний з x"""
    return x ** 2


def my_generator(begin, end, func):
    """Генерує значення від 'begin' до 'end', застосовуєчи функцію 'func'."""
    current = begin
    for _ in range(end):
        yield current
        current = func(current)


#Перевіряємо генератор
gen = my_generator(2, 4, pow)

print(isgenerator(gen))
print(list(gen))
