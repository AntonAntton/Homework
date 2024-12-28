def recurs_function(numb):
    if numb <= 1:
        return 1
    return numb + recurs_function(numb - 1)


print(recurs_function(10))