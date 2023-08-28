# * Замените классическое представление цикла for в примере на любую конструкцию, так чтоб результат оставался тот же.

def func_default(lst: list) -> None:
    for number in range(len(lst)):
        lst[number] *= number
    print(lst)


def new_func(lst: list) -> None:
    print(list(map(lambda x: x * lst.index(x), lst)))


lst = [2, 4, 5, 8, 9, 13]
func_default(lst.copy())
new_func(lst.copy())
