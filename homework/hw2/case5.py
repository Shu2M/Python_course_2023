# Можно переформулировать задачу следующим образом:
# нати количество способов разложить число n на слагаемые, так, чтобы каждое слагаемое отличалось от остальных
# не менее чем на 1
'''
def get_num_stairs_combination(num_blocks: int, comb: list = []):
    """
    Функция печатает все возможные комбинации лесенки из num_blocks блоков
    """
    if num_blocks == 0:
        print(comb)
    else:
        for i in range(1, num_blocks + 1):
            if not comb or comb[-1] < i:
                get_num_stairs_combination(num_blocks - i, comb + [i])

def f(n, max_floor=1000000000):
    """
    Эффективный алгоритм поиска кол-ва комбинаций лесенки, но я не разобрался как он работает
    """
    if n <= 1:
        return 1
    sum = 0
    for i in range(1, min(n, max_floor)+1):
        new_max_floor = i - 1
        if new_max_floor * (new_max_floor + 1) / 2 >= n - i:
            sum += f(n - i, new_max_floor)

    return sum
'''


def get_num_stairs_combination(num_blocks: int, next_layer: int = 0):
    if num_blocks == 0:
        return 1

    sum = 0
    for current_layer in range(1, num_blocks + 1):
        if next_layer < current_layer:
            sum += get_num_stairs_combination(num_blocks - current_layer, current_layer)

    return sum


a = 100
print(get_num_stairs_combination(a))

