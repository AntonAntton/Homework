
import string
import keyword
variable = input("Enter text: ")
print(variable)
if variable[0].isdigit():
    print("Error: Text cannot start with a number.")
elif any(x.isupper() for x in variable):
    print("Error: Uppercase letters are not allowed")
elif "__" in variable:
    print("Error: Double underscores '__' are not allowed.")
elif any(x in string.punctuation.replace("_", "") for x in variable):
    print("Error: Punctuation in not allowed.")
elif variable in keyword.kwlist:
    print("Error: Text cannot be a Python keyword")
else:
    print("Welcome")