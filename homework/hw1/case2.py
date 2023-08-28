# напишите функцию которая:
# a) принимает два списка
# b) возвращает длину самого длинного

def get_length_longest_list(list1: list, list2: list) -> int:
    len_list1 = len(list1)
    len_list2 = len(list2)
    return  len_list1 if len_list1 >= len_list2 else len_list2

a = []
b = []
print(get_length_longest_list(list1=a, list2=b))