def test_function():
    my_temp_str = "dsfdsfsfs"

    def inner_function():
        nonlocal my_temp_str
        my_temp_str = "fdsfdsfds"
        print(my_temp_str)

    print(my_temp_str)
    inner_function()
    print(my_temp_str)

my_temp_str = input('Enter a string:')
print(my_temp_str)
test_function()