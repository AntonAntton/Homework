a = input("Enter a: ")
b = input("Enter b: ")
try:
    a = int(a)
except (ValueError, TypeError):
    print("Exit(a) / TypeError(a)")
except Exception:
    print(1)
finally:
    print(a)
try:
    b = int(b)
except:
    print("Exit(b)")
print(a * b)

