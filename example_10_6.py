import random
import time


def my_time_decorator(some_round):
    def inner_function(function):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            nums = function(*args, **kwargs)
            end_time = time.time()
            print(f"Function {function.__name__} took {round((end_time - start_time), some_round)} sec")
            return nums

        return wrapper

    return inner_function


@my_time_decorator(4)
def add_elements_to_list(count_of_numbers):
    temp_list = []
    for i in range(count_of_numbers):
        random_number = random.randint(1, 100)
        temp_list.append(random_number)
    return temp_list


my_list = [1, 2, 3]

print(my_list)
my_list.extend(add_elements_to_list(10))
print(my_list)
