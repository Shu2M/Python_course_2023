def find_intersection(list_1: list, list_2: list) -> list:
    return list(set(list_1).intersection(list_2))


list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [2, 4, 6, 9, 10]
print(find_intersection(list_1, list_2))