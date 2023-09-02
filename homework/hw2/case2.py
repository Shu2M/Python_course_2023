def find_multiple(num: int or float) -> list:
    global lst
    return list(filter(lambda x: x % num == 0, lst))


lst = [i for i in range(100)]
print(find_multiple(5))
