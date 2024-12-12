my_list = [0, 1, 7, 2, 4, 8]
print(my_list)
my_list_1 = [my_list[i] for i in range(len(my_list)) if i % 2 == 0]
x = sum(my_list_1)
if my_list:
    y = my_list.pop()
    result = x * y
    print(result)
else:
    print(x)

my_list = [1, 3, 5]
print(my_list)
my_list_1 = [my_list[i] for i in range(len(my_list)) if i % 2 == 0]
x = sum(my_list_1)
if my_list:
    y = my_list.pop()
    result = x * y
    print(result)
else:
    print(x)

my_list = [6]
print(my_list)
my_list_1 = [my_list[i] for i in range(len(my_list)) if i % 2 == 0]
x = sum(my_list_1)
if my_list:
    y = my_list.pop()
    result = x * y
    print(result)
else:
    print(x)

my_list = []
print(my_list)
my_list_1 = [my_list[i] for i in range(len(my_list)) if i % 2 == 0]
x = sum(my_list_1)
if my_list:
    y = my_list.pop()
    result = x * y
    print(result)
else:
    print(x)
