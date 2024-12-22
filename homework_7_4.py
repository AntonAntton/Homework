def common_elements():
    elements = [n for n in range(100)]
    elements_3 = [n for n in elements if n % 3 == 0]
    elements_5 = [n for n in elements if n % 5 == 0]
    elements_union = set(elements_3) & set(elements_5)
    print(elements_union)
common_elements()