x = input("Enter number: ")
x = int(x)
q,w = divmod(x, 1000)
print(q)
q_1,w_1 = divmod(x, 1000)
print(w_1//100)
q_2,w_2 = divmod(x, 100)
print(w_2//10)
q_3,w_4 = divmod(x, 10)
print(w_4)


