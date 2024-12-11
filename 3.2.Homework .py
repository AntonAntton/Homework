my_list = []
n = int(input("How many numbers?: "))
for i in range(n):
    y = int(input(f"Enter numbers {i + 1}: "))
    my_list.append(y)
print(my_list)
last_element = my_list.pop()
my_list.insert(0, last_element)
print(my_list)






