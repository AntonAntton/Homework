my_number = int(input("Please, enter a number: "))
if 0 < my_number < 8640000:
    x, y = divmod(my_number, 86400)
    if x >= 0:
        print(f"{x} days", end=' ')
    x_1, y_1 = divmod(y, 3600)
    if 0 <= x_1 < 10:
        print(f"0{x_1}:", end='')
    else:
        print(f"{x_1}:", end='')
    x_2, y_2 = divmod(y_1, 60)
    if 0 <= x_2 < 10:
        print(f"0{x_2}:", end='')
    else:
        print(f"{x_2}:", end='')
    if 0 <= y_2 < 10:
        print(f"0{y_2}")
    else:
        print(f"{x_2}")