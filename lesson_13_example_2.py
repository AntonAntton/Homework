while True:
    try:
        a = int(input("A = "))
        break
    except ValueError:
        print("Error")

while True:
    try:
        b = int(input("B = "))
        break
    except ValueError:
        print("Error")

print(f"Square = ", a * b)
