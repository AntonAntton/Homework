x = int(input("number_1: "))
y = int(input("number_2: "))
z = input("Which operation? +,-,*,/: ")
if z == "+":
    result = x + y
elif z == "-":
    result = x - y
elif z == "*":
    result = x * y
elif z == "/":
    if y !=0:
        result = x / y
    else:
        result = "Error"
else:
    result = "invalid operation"
print (result)



