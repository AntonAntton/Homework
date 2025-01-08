def difference():
    # Запит від користувача
    my_numbers = input("Enter numbers: ").split(",")

    # Перетворюємо запит на ліст з числами (int або float)
    def parse_number(num):
        return int(num) if num.isdigit() else float(num)

    my_numbers = [parse_number(num for num in my_numbers)]
    
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
