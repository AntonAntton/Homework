feedback = input("your feedback: ")
words = len(feedback.split(" "))
words_1 = feedback.split()
print(words)
print(words_1)
if words <= 10:
    print("10%")
elif 10 < words <= 20:
    print("20%")
elif 20 < words <= 50:
    print("25%")
elif words > 50:
    print("30%")