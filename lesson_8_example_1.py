numbers = input("Enter your numbers: ").split()
numbers = [int(num) for num in numbers]


def get_list(numbers):
    return [num for ind, num in enumerate(numbers) if num not in numbers[:ind]]


num_list = get_list(numbers)
print("Unique numbers:", num_list)


def get_list_v2(numbers):
    seen = set()
    return [num for num in numbers if num not in seen and not seen.add(num)]


print(get_list_v2(numbers))