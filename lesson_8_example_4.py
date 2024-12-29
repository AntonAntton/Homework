def test_function(text, my_var, amount=3):
    return text.lower(), my_var / 2, amount



my_text = 'Some text'
my_amount = 5
test_function(my_text, my_amount)


print(test_function(amount=10, text=my_text, my_var=my_amount))
