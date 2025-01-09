def difference(*args):
    """
    Знаходимо різницю між максимальним і мінімальним значенням з лісту значень 
    Параметри: 
    *args: Невизначена кількість значень int або float
    Повертаємо: 
    Різниця між максимальним і мінімальним значенням int чи float
    """
    # Перевіряємо, чи є передані аргументи
    if not args:
        print("No numbers provided.")
        return

    # Перетворюємо аргументи на числа (int або float)
    def parse_number(num):
        return int(num) if isinstance(num, str) and num.isdigit() else float(num)

    numbers = [parse_number(num) for num in args]

    print("User numbers:", numbers)

    # Знаходимо максимальне і мінімальне значення
    max_val = max(numbers)
    min_val = min(numbers)

    # Розраховуємо різницю
    diff = max_val - min_val

    print("Maximum:", max_val)
    print("Minimum:", min_val)
    print("Difference:", diff)

# Введення користувача
user_input = input("Enter numbers separated by commas: ").split(",")
difference(*user_input)