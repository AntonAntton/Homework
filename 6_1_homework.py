import string
my_str = input("Enter a string: ")
print(my_str)
elem_1 = my_str[0]
elem_2 = my_str[2]
x_1 = (string.ascii_letters.index(elem_1))
x_2 = (string.ascii_letters.index(elem_2))
y_1 = string.ascii_letters[0:x_1]
y_2 = string.ascii_letters[x_2 + 1:]
z = [x for x in string.ascii_letters if x not in y_1 and x not in y_2]
print(''.join(z))