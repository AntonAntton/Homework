low = int(input('Enter a low number:'))
high = int(input('Enter a high number:'))
while low <= high:
    low += 1
    if not 10 <= low <= 15:
        print(low)
    else:
        continue