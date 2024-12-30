def add_one(my_numbers):
    number = int("".join(map(str, my_numbers)))
    number += 1
    return list(map(int, str(number)))


my_numbers = list(map(int, input("Enter your numbers(e.g. 1,2,3..): ").split(",")))
print(my_numbers)
result = add_one(my_numbers)
print("Result:", result)