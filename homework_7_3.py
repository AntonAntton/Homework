'''def correct_sentence(text):
     pass
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')'''


def correct_sentence():
    sentence = input("Please enter your sentence: ")
    sentence = sentence[0].upper() + sentence[1:]
    if sentence[-1] != ".":
        sentence += "."
    print(sentence)
correct_sentence()