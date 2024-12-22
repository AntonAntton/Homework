def say_hi():
    name = input("Please enter name: ")
    age = int(input("Please enter age: "))
    greeting = f"Hi. My name is {name} and I'm {age} years old."
    return greeting
print(say_hi())