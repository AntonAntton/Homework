'''def second_index(text, some_str):
  pass
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')'''

def second_index():
    n = 0
    my_text = input("Enter your text: ")
    element = input("Which element are you looking for?: ")
    first_index = my_text.find(element)
    if first_index == -1:
        print(f"element '{element}' is not found in your text")
        return
    second_index = my_text.find(element, first_index + 1)
    if second_index == -1:
        print(f"element '{element}' does not have second occurance in the text")
    else:
        print(f"The second occurence of '{element}' is at index {second_index}")
second_index()