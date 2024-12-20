import math

my_number = input("Please enter your number: ")
digits = [int(digit) for digit in my_number]
print(digits)

while len(digits) > 1:
    product = math.prod(digits) 
    print(f"Product of digits: {product}")
    digits = [int(digit) for digit in str(product)]

print(f"Final single-digit result: {digits[0]}")

