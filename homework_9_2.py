def difference():
    """
    Знаходимо різницю між максимальним і мінімальним значенням з лісту значень 
    Параметри: 
    my_numbers(list): ліст з значеннями int або float
    Повертаємо: 
    Різниця між максимальним і мінімальним значенням int чи float
    """
    # Запит від користувача
    my_numbers = input("Enter numbers: ").split(",")

    # Перетворюємо запит на ліст з числами (int або float)
    def parse_number(num):
        return int(num) if num.isdigit() else float(num)

    my_numbers = [parse_number(num) for num in my_numbers]
    
    print("User numbers:", my_numbers)

    # Знаходимо максимальне і мінімальне значення
    max_val = max(my_numbers)
    min_val = min(my_numbers)

    # Розраховуємо різницю
    diff = max_val - min_val

    print("Maximum:", max_val)
    print("Minimum:", min_val)
    print("Difference:", diff)

difference()
