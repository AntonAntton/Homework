first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
math_operation = input("Enter math operation: ")


def add(first_num, second_num):
    return first_num + second_num


def subtract(first_num, second_num):
    return first_num - second_num


def multiply(first_num, second_num):
    return first_num * second_num


def divide(first_num, second_num):
    if second_num != 0:
        return first_num / second_num
    else:
        return "can't divide on 0 "


def math_result(math_operation):
    if math_operation == "+":
        print(add(first_num, second_num))
    elif math_operation == "-":
        print(subtract(first_num, second_num))
    elif math_operation == "*":
        print(multiply(first_num, second_num))
    elif math_operation == "/":
        print(divide(first_num, second_num))

math_result(math_operation)
