def is_palindrome(text):
    return text == text[::-1]


my_text = input("Enter your text: ")

print(is_palindrome(my_text))