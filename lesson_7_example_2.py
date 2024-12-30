import string

user_text = input("Enter text: ")
user_text = user_text.lower()
user_text = user_text.translate(str.maketrans("", "", string.punctuation))

word_count ={}

words = user_text.split()[:1000]
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("result:")
for word, count in word_count.items():
    print(f"{word}: {count}")