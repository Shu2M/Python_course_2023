def main(a, b):
    return a + b


def arg(a: int or float, b: int or float, c=2, d=1) -> int or float:
    return a + b + c + d


def range_arg(a: str, b: str, c: str, d: str) -> str:
    return a + ' ' + b + ' ' + c + ' ' + d


def get_square_data(square_edge_length: int or float) -> tuple:
    return square_edge_length * 4, square_edge_length * square_edge_length


def add(*args):
    value = 0

    for item in args:
        if isinstance(item, (int, float)):
            value += item

    return value


def print_kwargs(**kwargs):
    print(kwargs)


total = add(1, 'function', 2, 3, 4, 'python', 5.6, 'kargs')
print('total: ', total)
print_kwargs(kone='One', ktwo='Two')


