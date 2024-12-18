my_dict = {'Franco': ['book1', 'book2', 'book3'],}
print(my_dict['Franco'])
my_dict['Ukrainka'] = ['book21', 'book22', 'book23']
print(my_dict)
print(len(my_dict))
my_dict['Ukrainka'] = ['book31', 'book32', 'book33']
print(my_dict['Ukrainka'])
my_dict['Ukrainka'][1] = 'book34'
print(my_dict)
phonebook = {
    'Max': {
        'phone': '+0',
        'exp': 3,
        'portfolio': ["fdsfsdfsdfsd", "fdsfdsfdsf"],
        'email': 'Email',
    },
    'Ivan': {
        'phone': '+0',
        'exp': 3,
        'portfolio': ["fdsfsdfsdfsd", "fdsfdsfdsf"],
        'email': 'Email',
    }
}
print(phonebook)
print(phonebook['Max']['email'])
print(type(phonebook['Ivan']['portfolio']))



