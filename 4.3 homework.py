"""
[1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
[1, 1, 2, 1] == [1, 2, 2]
[6, 3, 7] == [6, 7, 3]
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 9]
print(my_list)
x = my_list[:1]
y = my_list[2:3]
z = my_list[len(my_list) - 2:len(my_list) - 1]
result = x + y + z
print(result)

my_list = [1, 1, 2, 1]
print(my_list)
x = my_list[:1]
y = my_list[2:3]
z = my_list[len(my_list) - 2:len(my_list) - 1]
result = x + y + z
print(result)

my_list = [6, 3, 7]
print(my_list)
x = my_list[:1]
y = my_list[2:3]
z = my_list[len(my_list) - 2:len(my_list) - 1]
result = x + y + z
print(result)