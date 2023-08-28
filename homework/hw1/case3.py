# Напишите функцию которая:
# a) принимает список с произвольными значениями
# b) добавляет к нему произвольное значение
# c) возвращает результирующий список
from typing import Any

def append_to_list(l: list, new_element: Any) -> list:
    l.append(new_element)
    return l

a = ['fd', 4, [4, 'trt', 550], 5.3, 7.65]
b = append_to_list(a, {'f': [45]})
print(b)