# Функция на вход получает список, состоящий из 5 произвольных чисел. Найти количество положительных чисел среди них.

def find_num_pos_numbers_in_list(array: list) -> int:
    return len(list(filter(lambda x: x > 0, array)))

print(find_num_pos_numbers_in_list([1, 2, 3, 4, 5]))
print(find_num_pos_numbers_in_list([-1, 2, 3, 4, 5]))
print(find_num_pos_numbers_in_list([1, -2, 3, -4, 5]))
print(find_num_pos_numbers_in_list([-1, -2, -3, -4, -5]))