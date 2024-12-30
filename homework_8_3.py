from collections import Counter


def find_unique_value(my_list):
    count = Counter(my_list)
    unique_numbers = [num for num, x in count.items() if x == 1]

    if len(unique_numbers) == 1:
        return unique_numbers[0]
    else:
        return "More than one or none unique number found"


my_list = list(input("Enter your numbers(e.g. 1,2..): ").split(","))
print(find_unique_value(my_list))

