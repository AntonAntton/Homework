matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)

summ_element = 0
for row in matrix:
    row_sum = sum(row)
    summ_element += row_sum
    print(f"summ row:{row}, {row_sum}")
print(f"summ all elements: {summ_element}")