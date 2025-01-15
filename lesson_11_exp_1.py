def selection_sort(list_of_numbers):
    if len(list_of_numbers) <= 1:
        return list_of_numbers
    else:
        for element in range(len(list_of_numbers)):
            min_index = element
            for j_element in range(element + 1, len(list_of_numbers)):
                if list_of_numbers[j_element] < list_of_numbers[min_index]:
                    min_index = j_element

            list_of_numbers[element], list_of_numbers[min_index] = list_of_numbers[min_index], list_of_numbers[element]

    return list_of_numbers


some_list = [1, 5, 7, 2, 6, 8, 9, 10, 3, 4]

selection_sort(some_list)

print("Selection sort:", some_list)


def insertion_sort(list_of_numbers):
    for element in range(1, len(list_of_numbers)):
        key = list_of_numbers[element]
        j = element - 1
        while j >= 0 and list_of_numbers[j] > key:
            list_of_numbers[j + 1] = list_of_numbers[j]
            j -= 1

        list_of_numbers[j + 1] = key

insertion_sort(some_list)
print("Insertion sort", some_list)



